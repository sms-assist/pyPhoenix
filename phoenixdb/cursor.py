# Copyright 2015 Lukas Lalinsky
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import base64
import datetime
import collections
from decimal import Decimal
from phoenixdb.types import Binary
from phoenixdb.errors import InternalError, ProgrammingError
from common_pb2 import Rep, TypedValue

__all__ = ['Cursor', 'ColumnDescription']

logger = logging.getLogger(__name__)

ColumnDescription = collections.namedtuple('ColumnDescription', 'name type_code display_size internal_size precision scale null_ok')
"""Named tuple for representing results from :attr:`Cursor.description`."""


def time_from_java_sql_time(n):
    dt = datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=n)
    return dt.time()


def time_to_java_sql_time(t):
    return ((t.hour * 60 + t.minute) * 60 + t.second) * 1000 + t.microsecond / 1000


def date_from_java_sql_date(n):
    return datetime.date(1970, 1, 1) + datetime.timedelta(days=n)


def date_to_java_sql_date(d):
    if isinstance(d, datetime.datetime):
        d = d.date()
    td = d - datetime.date(1970, 1, 1)
    return td.days


def datetime_from_java_sql_timestamp(n):
    return datetime.datetime(1970, 1, 1) + datetime.timedelta(milliseconds=n)


def datetime_to_java_sql_timestamp(d):
    td = d - datetime.datetime(1970, 1, 1)
    return td.microseconds / 1000 + (td.seconds + td.days * 24 * 3600) * 1000


def typedValueToNative(v):
    if Rep.Name(v.type) == "BOOLEAN" or Rep.Name(v.type) == "PRIMITIVE_BOOLEAN":
        return v.bool_value

    elif Rep.Name(v.type) == "STRING" or Rep.Name(v.type) == "PRIMITIVE_CHAR" or Rep.Name(v.type) == "CHARACTER" or Rep.Name(v.type) == "BIG_DECIMAL":
        return v.string_value

    elif Rep.Name(v.type) == "FLOAT" or Rep.Name(v.type) == "PRIMITIVE_FLOAT" or Rep.Name(v.type) == "DOUBLE" or Rep.Name(v.type) == "PRIMITIVE_DOUBLE":
        return v.double_value

    elif Rep.Name(v.type) == "LONG" or Rep.Name(v.type) == "PRIMITIVE_LONG" or Rep.Name(v.type) == "INTEGER" or Rep.Name(v.type) == "PRIMITIVE_INT" or \
                    Rep.Name(v.type) == "BIG_INTEGER" or Rep.Name(v.type) == "NUMBER" or Rep.Name(v.type) == "BYTE" or Rep.Name(v.type) == "PRIMITIVE_BYTE" or \
                    Rep.Name(v.type) == "SHORT" or Rep.Name(v.type) == "PRIMITIVE_SHORT":
        return v.number_value

    elif Rep.Name(v.type) == "BYTE_STRING":
        return v.bytes_value

    else:
        return None

class Cursor(object):
    """Database cursor for executing queries and iterating over results.
    
    You should not construct this object manually, use :meth:`Connection.cursor() <phoenixdb.connection.Connection.cursor>` instead.
    """

    arraysize = 1
    """
    Read/write attribute specifying the number of rows to fetch
    at a time with :meth:`fetchmany`. It defaults to 1 meaning to
    fetch a single row at a time.
    """

    itersize = 2000
    """
    Read/write attribute specifying the number of rows to fetch
    from the backend at each network roundtrip during iteration
    on the cursor. The default is 2000.
    """

    def __init__(self, connection, id=None):
        self._connection = connection
        self._id = id
        self._signature = None
        self._column_data_types = []
        self._frame = None
        self._pos = None
        self._closed = False
        self.arraysize = self.__class__.arraysize
        self.itersize = self.__class__.itersize
        self._updatecount = -1

    def __del__(self):
        if not self._connection._closed and not self._closed:
            self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self._closed:
            self.close()

    def __iter__(self):
        return self

    def next(self):
        row = self.fetchone()
        if row is None:
            raise StopIteration
        return row

    def close(self):
        """Closes the cursor.
        No further operations are allowed once the cursor is closed.

        If the cursor is used in a ``with`` statement, this method will
        be automatically called at the end of the ``with`` block.
        """
        if self._closed:
            raise ProgrammingError('the cursor is already closed')
        if self._id is not None:
            self._connection._client.closeStatement(self._connection._id, self._id)
            self._id = None
        self._signature = None
        self._column_data_types = []
        self._frame = None
        self._pos = None
        self._closed = True

    @property
    def closed(self):
        """Read-only attribute specifying if the cursor is closed or not."""
        return self._closed

    @property
    def description(self):
        if self._signature is None:
            return None
        description = []
        for column in self._signature.columns:
            description.append(ColumnDescription(
                column.column_name,
                column.type.name,
                column.display_size,
                None,
                column.precision,
                column.scale,
                bool(column.nullable),
            ))
        return description

    def _set_id(self, id):
        if self._id is not None and self._id != id:
            self._connection._client.closeStatement(self._connection._id, self._id)
        self._id = id

    def _set_signature(self, signature):
        self._signature = signature
        self._column_data_types = []
        self._parameter_data_types = []
        if signature is None:
            return
        identity = lambda value: value
        for i, column in enumerate(signature.columns):
            if column.column_class_name == 'java.math.BigDecimal':
                self._column_data_types.append((i, Decimal))
            elif column.column_class_name == 'java.lang.Float' or column.column_class_name == 'java.lang.Double':
                self._column_data_types.append((i, float))
            elif column.column_class_name == 'java.sql.Time':
                self._column_data_types.append((i, time_from_java_sql_time))
            elif column.column_class_name == 'java.sql.Date':
                self._column_data_types.append((i, date_from_java_sql_date))
            elif column.column_class_name == 'java.sql.Timestamp':
                self._column_data_types.append((i, datetime_from_java_sql_timestamp))
            elif column.type.name == 'BINARY':
                self._column_data_types.append((i, base64.b64decode))
            else:
                self._column_data_types.append((i, None))

        for parameter in signature.parameters:
            if parameter.class_name == 'java.math.BigDecimal':
                self._parameter_data_types.append(('NUMBER', None, "number_value"))
            elif parameter.class_name == 'java.lang.Float':
                self._parameter_data_types.append(('FLOAT', None, "double_value"))
            elif parameter.class_name == 'java.lang.Double':
                self._parameter_data_types.append(('DOUBLE', None, "double_value"))
            elif parameter.class_name == 'java.lang.Long':
                self._parameter_data_types.append(('LONG', None, "number_value"))
            elif parameter.class_name == 'java.lang.Integer':
                self._parameter_data_types.append(('INTEGER', None, "number_value"))
            elif parameter.class_name == 'java.lang.Short':
                self._parameter_data_types.append(('SHORT', None, "number_value"))
            elif parameter.class_name == 'java.lang.Byte':
                self._parameter_data_types.append(('BYTE', None, "bytes_value"))
            elif parameter.class_name == 'java.lang.Boolean':
                self._parameter_data_types.append(('BOOLEAN', None, "bool_value"))
            elif parameter.class_name == 'java.lang.String':
                self._parameter_data_types.append(('STRING', None, "string_value"))
            elif parameter.class_name == 'java.sql.Time':
                self._parameter_data_types.append(('JAVA_SQL_TIME', time_to_java_sql_time, "number_value"))
            elif parameter.class_name == 'java.sql.Date':
                self._parameter_data_types.append(('JAVA_SQL_DATE', date_to_java_sql_date, "number_value"))
            elif parameter.class_name == 'java.sql.Timestamp':
                self._parameter_data_types.append(('JAVA_SQL_TIMESTAMP', datetime_to_java_sql_timestamp, "number_value"))
            elif parameter.class_name == '[B':
                self._parameter_data_types.append(('BYTE_STRING', Binary, "bytes_value"))
            #elif parameter.class_name == 'org.apache.phoenix.schema.types.PhoenixArray':
            #    self._parameter_data_types.append(('ARRAY', None))
            else:
                self._parameter_data_types.append(('NULL', None))

    def _transform_parameters(self, parameters):
        typed_parameters = []
        for value, data_type in zip(parameters, self._parameter_data_types):

            if value is None:
                typed_parameters.append(TypedValue(null=True, type=Rep.Value('NULL')))
            else:
                v = TypedValue()
                v.type = Rep.Value(data_type[0])
                if data_type[1] is not None:
                    setattr(v, data_type[2], data_type[1](value))
                else:
                    setattr(v, data_type[2], value)

                typed_parameters.append(v)
        return typed_parameters

    def _set_frame(self, frame):
        self._frame = frame
        self._pos = None
        if frame is not None:
            if frame.rows:
                self._pos = 0
            elif not frame.done:
                raise InternalError('got an empty frame, but the statement is not done yet')

    def _fetch_next_frame(self):
        offset = self._frame.offset + len(self._frame.rows)
        frame = self._connection._client.fetch(self._connection._id, self._id,
            offset=offset, fetchMaxRowCount=self.itersize)
        self._set_frame(frame)

    def _process_results(self, results):
        if results:
            result = results[0]
            if result.own_statement:
                self._set_id(result.statement_id)
            self._set_signature(result.signature)
            self._set_frame(result.first_frame)
            self._updatecount = result.update_count

    def execute(self, operation, parameters=None):
        if self._closed:
            raise ProgrammingError('the cursor is already closed')
        self._updatecount = -1
        self._set_frame(None)
        if parameters is None or len(parameters) == 0:
            if self._id is None:
                self._set_id(self._connection._client.createStatement(self._connection._id))
            results = self._connection._client.prepareAndExecute(self._connection._id, self._id,
                operation, maxRowCount=self.itersize)
            self._process_results(results)
        else:
            statement = self._connection._client.prepare(self._connection._id,
                operation, maxRowCount=self.itersize)
            self._set_id(statement.id)
            self._set_signature(statement.signature)
            results = self._connection._client.execute(self._connection._id, self._id,self._signature,
                    self._transform_parameters(parameters), maxRowCount=self.itersize)
            self._process_results(results)


    def executemany(self, operation, seq_of_parameters):
        if self._closed:
            raise ProgrammingError('the cursor is already closed')
        self._updatecount = -1
        self._set_frame(None)
        statement = self._connection._client.prepare(self._connection._id,
            operation, maxRowCount=0)
        self._set_id(statement.id)
        self._set_signature(statement.signature)
        for parameters in seq_of_parameters:
            self._connection._client.execute(self._connection._id, self._id,
                    self._transform_parameters(parameters),
                    maxRowCount=0)


    def fetchone(self):
        result_row = []
        if self._frame is None:
            raise ProgrammingError('no select statement was executed')
        if self._pos is None:
            return None
        rows = self._frame.rows
        row = rows[self._pos]
        self._pos += 1
        if self._pos >= len(rows):
            self._pos = None
            if not self._frame.done:
                self._fetch_next_frame()
        for i, data_type in self._column_data_types:
            value = row.value[i].scalar_value
            if data_type is not None and value.null is not True:
                result_row.append(data_type(typedValueToNative(value)))
            else:
                result_row.append(typedValueToNative(value))

        return tuple(result_row)

    def fetchmany(self, size=None):
        if size is None:
            size = self.arraysize
        rows = []
        while size > 0:
            row = self.fetchone()
            if row is None:
                break
            rows.append(row)
            size -= 1
        return rows

    def fetchall(self):
        rows = []
        while True:
            row = self.fetchone()
            if row is None:
                break
            rows.append(row)
        return rows

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, size, column=None):
        pass

    @property
    def connection(self):
        """Read-only attribute providing access to the :class:`Connection <phoenixdb.connection.Connection>` object this cursor was created from."""
        return self._connection


    @property
    def rowcount(self):
        """Read-only attribute specifying the number of rows affected by
        the last executed DML statement or -1 if the number cannot be
        determined. Note that this will always be set to -1 for select
        queries."""
        return self._updatecount

    @property
    def rownumber(self):
        """Read-only attribute providing the current 0-based index of the
        cursor in the result set or ``None`` if the index cannot be
        determined.
        
        The index can be seen as index of the cursor in a sequence
        (the result set). The next fetch operation will fetch the
        row indexed by :attr:`rownumber` in that sequence.
        """
        if self._frame is not None and self._pos is not None:
            return self._frame.offset + self._pos
        return self._pos
