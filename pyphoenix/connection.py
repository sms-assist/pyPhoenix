# Copyright 2016 Dimitri Capitaine
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
import uuid
import weakref
from pyphoenix import errors
from pyphoenix.cursor import Cursor
from pyphoenix.errors import ProgrammingError
from .common_pb2 import ConnectionProperties

__all__ = ['Connection']

logger = logging.getLogger(__name__)


class Connection(object):
    """Database connection.
    
    You should not construct this object manually, use :func:`~pyphoenix.connect` instead.
    """

    def __init__(self, client, **kwargs):
        self._client = client
        self._closed = False
        self._cursors = []
        self.open()
        self.set_session(**kwargs)

    def __del__(self):
        if not self._closed:
            self.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if not self._closed:
            self.close()

    def open(self):
        """Opens the connection."""
        self._id = str(uuid.uuid4())
        self._client.openConnection(self._id)

    def close(self):
        """Closes the connection.
        No further operations are allowed, either on the connection or any
        of its cursors, once the connection is closed.

        If the connection is used in a ``with`` statement, this method will
        be automatically called at the end of the ``with`` block.
        """
        if self._closed:
            raise ProgrammingError('the connection is already closed')
        for cursor_ref in self._cursors:
            cursor = cursor_ref()
            if cursor is not None and not cursor._closed:
                cursor.close()
        self._client.closeConnection(self._id)
        self._client.close()
        self._closed = True

    @property
    def closed(self):
        """Read-only attribute specifying if the connection is closed or not."""
        return self._closed

    def commit(self):
        """Commits pending database changes.

        Currently, this does nothing, because the RPC does not support
        transactions. Only defined for DB API 2.0 compatibility.
        You need to use :attr:`autocommit` mode.
        """
        if self._closed:
            raise ProgrammingError('the connection is already closed')

    def cursor(self):
        """Creates a new cursor.

        :returns:
            A :class:`~pyphoenix.cursor.Cursor` object.
        """
        if self._closed:
            raise ProgrammingError('the connection is already closed')
        cursor = Cursor(self)
        self._cursors.append(weakref.ref(cursor, self._cursors.remove))
        return cursor

    def set_session(self, autocommit=None, readonly=None):
        """Sets one or more parameters in the current connection.
        
        :param autocommit:
            Switch the connection to autocommit mode. With the current
            version, you need to always enable this, because
            :meth:`commit` is not implemented.
        
        :param readonly:
            Switch the connection to read-only mode.
        """
        props = conn_props = ConnectionProperties(has_auto_commit=False, has_read_only=False)
        if autocommit is not None:
            props.auto_commit = bool(autocommit)
            props.has_auto_commit = True
        if readonly is not None:
            props.read_only = bool(readonly)
            props.has_read_only = True
        props = self._client.connectionSync(self._id, props)
        self._autocommit = props.auto_commit
        self._readonly = props.read_only

    @property
    def autocommit(self):
        """Read/write attribute for switching the connection's autocommit mode."""
        return self._autocommit

    @autocommit.setter
    def autocommit(self, value):
        if self._closed:
            raise ProgrammingError('the connection is already closed')
        props = self._client.connectionSync(self._id, {'auto_commit': bool(value)})
        self._autocommit = props['auto_commit']

    @property
    def readonly(self):
        """Read/write attribute for switching the connection's readonly mode."""
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        if self._closed:
            raise ProgrammingError('the connection is already closed')
        props = self._client.connectionSync(self._id, {'read_only': bool(value)})
        self._readonly = props['read_only']


for name in errors.__all__:
    setattr(Connection, name, getattr(errors, name))
