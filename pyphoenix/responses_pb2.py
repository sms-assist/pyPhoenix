# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyphoenix/responses.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyphoenix import common_pb2 as pyphoenix_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyphoenix/responses.proto',
  package='pyphoenix',
  syntax='proto3',
  serialized_pb=_b('\n\x19pyphoenix/responses.proto\x12\tpyphoenix\x1a\x16pyphoenix/common.proto\"\xe7\x01\n\x11ResultSetResponse\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x14\n\x0cstatement_id\x18\x02 \x01(\r\x12\x15\n\rown_statement\x18\x03 \x01(\x08\x12\'\n\tsignature\x18\x04 \x01(\x0b\x32\x14.pyphoenix.Signature\x12%\n\x0b\x66irst_frame\x18\x05 \x01(\x0b\x32\x10.pyphoenix.Frame\x12\x14\n\x0cupdate_count\x18\x06 \x01(\x04\x12(\n\x08metadata\x18\x07 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"\x85\x01\n\x0f\x45xecuteResponse\x12-\n\x07results\x18\x01 \x03(\x0b\x32\x1c.pyphoenix.ResultSetResponse\x12\x19\n\x11missing_statement\x18\x02 \x01(\x08\x12(\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"j\n\x0fPrepareResponse\x12-\n\tstatement\x18\x01 \x01(\x0b\x32\x1a.pyphoenix.StatementHandle\x12(\n\x08metadata\x18\x02 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"\x8e\x01\n\rFetchResponse\x12\x1f\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x10.pyphoenix.Frame\x12\x19\n\x11missing_statement\x18\x02 \x01(\x08\x12\x17\n\x0fmissing_results\x18\x03 \x01(\x08\x12(\n\x08metadata\x18\x04 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"p\n\x17\x43reateStatementResponse\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x14\n\x0cstatement_id\x18\x02 \x01(\r\x12(\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"B\n\x16\x43loseStatementResponse\x12(\n\x08metadata\x18\x01 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"B\n\x16OpenConnectionResponse\x12(\n\x08metadata\x18\x01 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"C\n\x17\x43loseConnectionResponse\x12(\n\x08metadata\x18\x01 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"w\n\x16\x43onnectionSyncResponse\x12\x33\n\nconn_props\x18\x01 \x01(\x0b\x32\x1f.pyphoenix.ConnectionProperties\x12(\n\x08metadata\x18\x02 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"\x93\x01\n\x17\x44\x61tabasePropertyElement\x12(\n\x03key\x18\x01 \x01(\x0b\x32\x1b.pyphoenix.DatabaseProperty\x12$\n\x05value\x18\x02 \x01(\x0b\x32\x15.pyphoenix.TypedValue\x12(\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"w\n\x18\x44\x61tabasePropertyResponse\x12\x31\n\x05props\x18\x01 \x03(\x0b\x32\".pyphoenix.DatabasePropertyElement\x12(\n\x08metadata\x18\x02 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"\xca\x01\n\rErrorResponse\x12\x12\n\nexceptions\x18\x01 \x03(\t\x12\x16\n\x0ehas_exceptions\x18\x07 \x01(\x08\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12%\n\x08severity\x18\x03 \x01(\x0e\x32\x13.pyphoenix.Severity\x12\x12\n\nerror_code\x18\x04 \x01(\r\x12\x11\n\tsql_state\x18\x05 \x01(\t\x12(\n\x08metadata\x18\x06 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"p\n\x13SyncResultsResponse\x12\x19\n\x11missing_statement\x18\x01 \x01(\x08\x12\x14\n\x0cmore_results\x18\x02 \x01(\x08\x12(\n\x08metadata\x18\x03 \x01(\x0b\x32\x16.pyphoenix.RpcMetadata\"%\n\x0bRpcMetadata\x12\x16\n\x0eserver_address\x18\x01 \x01(\t\"\x10\n\x0e\x43ommitResponse\"\x12\n\x10RollbackResponse\"\x9f\x01\n\x14\x45xecuteBatchResponse\x12\x15\n\rconnection_id\x18\x01 \x01(\t\x12\x14\n\x0cstatement_id\x18\x02 \x01(\r\x12\x15\n\rupdate_counts\x18\x03 \x03(\x04\x12\x19\n\x11missing_statement\x18\x04 \x01(\x08\x12(\n\x08metadata\x18\x05 \x01(\x0b\x32\x16.pyphoenix.RpcMetadatab\x06proto3')
  ,
  dependencies=[pyphoenix_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESULTSETRESPONSE = _descriptor.Descriptor(
  name='ResultSetResponse',
  full_name='pyphoenix.ResultSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='pyphoenix.ResultSetResponse.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='statement_id', full_name='pyphoenix.ResultSetResponse.statement_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='own_statement', full_name='pyphoenix.ResultSetResponse.own_statement', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='pyphoenix.ResultSetResponse.signature', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_frame', full_name='pyphoenix.ResultSetResponse.first_frame', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_count', full_name='pyphoenix.ResultSetResponse.update_count', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.ResultSetResponse.metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=296,
)


_EXECUTERESPONSE = _descriptor.Descriptor(
  name='ExecuteResponse',
  full_name='pyphoenix.ExecuteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='pyphoenix.ExecuteResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_statement', full_name='pyphoenix.ExecuteResponse.missing_statement', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.ExecuteResponse.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=432,
)


_PREPARERESPONSE = _descriptor.Descriptor(
  name='PrepareResponse',
  full_name='pyphoenix.PrepareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='statement', full_name='pyphoenix.PrepareResponse.statement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.PrepareResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=434,
  serialized_end=540,
)


_FETCHRESPONSE = _descriptor.Descriptor(
  name='FetchResponse',
  full_name='pyphoenix.FetchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='pyphoenix.FetchResponse.frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_statement', full_name='pyphoenix.FetchResponse.missing_statement', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_results', full_name='pyphoenix.FetchResponse.missing_results', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.FetchResponse.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=685,
)


_CREATESTATEMENTRESPONSE = _descriptor.Descriptor(
  name='CreateStatementResponse',
  full_name='pyphoenix.CreateStatementResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='pyphoenix.CreateStatementResponse.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='statement_id', full_name='pyphoenix.CreateStatementResponse.statement_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.CreateStatementResponse.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=799,
)


_CLOSESTATEMENTRESPONSE = _descriptor.Descriptor(
  name='CloseStatementResponse',
  full_name='pyphoenix.CloseStatementResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.CloseStatementResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=801,
  serialized_end=867,
)


_OPENCONNECTIONRESPONSE = _descriptor.Descriptor(
  name='OpenConnectionResponse',
  full_name='pyphoenix.OpenConnectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.OpenConnectionResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=869,
  serialized_end=935,
)


_CLOSECONNECTIONRESPONSE = _descriptor.Descriptor(
  name='CloseConnectionResponse',
  full_name='pyphoenix.CloseConnectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.CloseConnectionResponse.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=937,
  serialized_end=1004,
)


_CONNECTIONSYNCRESPONSE = _descriptor.Descriptor(
  name='ConnectionSyncResponse',
  full_name='pyphoenix.ConnectionSyncResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conn_props', full_name='pyphoenix.ConnectionSyncResponse.conn_props', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.ConnectionSyncResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1006,
  serialized_end=1125,
)


_DATABASEPROPERTYELEMENT = _descriptor.Descriptor(
  name='DatabasePropertyElement',
  full_name='pyphoenix.DatabasePropertyElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='pyphoenix.DatabasePropertyElement.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='pyphoenix.DatabasePropertyElement.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.DatabasePropertyElement.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1275,
)


_DATABASEPROPERTYRESPONSE = _descriptor.Descriptor(
  name='DatabasePropertyResponse',
  full_name='pyphoenix.DatabasePropertyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='props', full_name='pyphoenix.DatabasePropertyResponse.props', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.DatabasePropertyResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1277,
  serialized_end=1396,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='pyphoenix.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exceptions', full_name='pyphoenix.ErrorResponse.exceptions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_exceptions', full_name='pyphoenix.ErrorResponse.has_exceptions', index=1,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='pyphoenix.ErrorResponse.error_message', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='severity', full_name='pyphoenix.ErrorResponse.severity', index=3,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='pyphoenix.ErrorResponse.error_code', index=4,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sql_state', full_name='pyphoenix.ErrorResponse.sql_state', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.ErrorResponse.metadata', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1399,
  serialized_end=1601,
)


_SYNCRESULTSRESPONSE = _descriptor.Descriptor(
  name='SyncResultsResponse',
  full_name='pyphoenix.SyncResultsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='missing_statement', full_name='pyphoenix.SyncResultsResponse.missing_statement', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='more_results', full_name='pyphoenix.SyncResultsResponse.more_results', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.SyncResultsResponse.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1603,
  serialized_end=1715,
)


_RPCMETADATA = _descriptor.Descriptor(
  name='RpcMetadata',
  full_name='pyphoenix.RpcMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='server_address', full_name='pyphoenix.RpcMetadata.server_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1717,
  serialized_end=1754,
)


_COMMITRESPONSE = _descriptor.Descriptor(
  name='CommitResponse',
  full_name='pyphoenix.CommitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1756,
  serialized_end=1772,
)


_ROLLBACKRESPONSE = _descriptor.Descriptor(
  name='RollbackResponse',
  full_name='pyphoenix.RollbackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1774,
  serialized_end=1792,
)


_EXECUTEBATCHRESPONSE = _descriptor.Descriptor(
  name='ExecuteBatchResponse',
  full_name='pyphoenix.ExecuteBatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='pyphoenix.ExecuteBatchResponse.connection_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='statement_id', full_name='pyphoenix.ExecuteBatchResponse.statement_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='update_counts', full_name='pyphoenix.ExecuteBatchResponse.update_counts', index=2,
      number=3, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='missing_statement', full_name='pyphoenix.ExecuteBatchResponse.missing_statement', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='pyphoenix.ExecuteBatchResponse.metadata', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1795,
  serialized_end=1954,
)

_RESULTSETRESPONSE.fields_by_name['signature'].message_type = pyphoenix_dot_common__pb2._SIGNATURE
_RESULTSETRESPONSE.fields_by_name['first_frame'].message_type = pyphoenix_dot_common__pb2._FRAME
_RESULTSETRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_EXECUTERESPONSE.fields_by_name['results'].message_type = _RESULTSETRESPONSE
_EXECUTERESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_PREPARERESPONSE.fields_by_name['statement'].message_type = pyphoenix_dot_common__pb2._STATEMENTHANDLE
_PREPARERESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_FETCHRESPONSE.fields_by_name['frame'].message_type = pyphoenix_dot_common__pb2._FRAME
_FETCHRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_CREATESTATEMENTRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_CLOSESTATEMENTRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_OPENCONNECTIONRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_CLOSECONNECTIONRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_CONNECTIONSYNCRESPONSE.fields_by_name['conn_props'].message_type = pyphoenix_dot_common__pb2._CONNECTIONPROPERTIES
_CONNECTIONSYNCRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_DATABASEPROPERTYELEMENT.fields_by_name['key'].message_type = pyphoenix_dot_common__pb2._DATABASEPROPERTY
_DATABASEPROPERTYELEMENT.fields_by_name['value'].message_type = pyphoenix_dot_common__pb2._TYPEDVALUE
_DATABASEPROPERTYELEMENT.fields_by_name['metadata'].message_type = _RPCMETADATA
_DATABASEPROPERTYRESPONSE.fields_by_name['props'].message_type = _DATABASEPROPERTYELEMENT
_DATABASEPROPERTYRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_ERRORRESPONSE.fields_by_name['severity'].enum_type = pyphoenix_dot_common__pb2._SEVERITY
_ERRORRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_SYNCRESULTSRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
_EXECUTEBATCHRESPONSE.fields_by_name['metadata'].message_type = _RPCMETADATA
DESCRIPTOR.message_types_by_name['ResultSetResponse'] = _RESULTSETRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteResponse'] = _EXECUTERESPONSE
DESCRIPTOR.message_types_by_name['PrepareResponse'] = _PREPARERESPONSE
DESCRIPTOR.message_types_by_name['FetchResponse'] = _FETCHRESPONSE
DESCRIPTOR.message_types_by_name['CreateStatementResponse'] = _CREATESTATEMENTRESPONSE
DESCRIPTOR.message_types_by_name['CloseStatementResponse'] = _CLOSESTATEMENTRESPONSE
DESCRIPTOR.message_types_by_name['OpenConnectionResponse'] = _OPENCONNECTIONRESPONSE
DESCRIPTOR.message_types_by_name['CloseConnectionResponse'] = _CLOSECONNECTIONRESPONSE
DESCRIPTOR.message_types_by_name['ConnectionSyncResponse'] = _CONNECTIONSYNCRESPONSE
DESCRIPTOR.message_types_by_name['DatabasePropertyElement'] = _DATABASEPROPERTYELEMENT
DESCRIPTOR.message_types_by_name['DatabasePropertyResponse'] = _DATABASEPROPERTYRESPONSE
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
DESCRIPTOR.message_types_by_name['SyncResultsResponse'] = _SYNCRESULTSRESPONSE
DESCRIPTOR.message_types_by_name['RpcMetadata'] = _RPCMETADATA
DESCRIPTOR.message_types_by_name['CommitResponse'] = _COMMITRESPONSE
DESCRIPTOR.message_types_by_name['RollbackResponse'] = _ROLLBACKRESPONSE
DESCRIPTOR.message_types_by_name['ExecuteBatchResponse'] = _EXECUTEBATCHRESPONSE

ResultSetResponse = _reflection.GeneratedProtocolMessageType('ResultSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSETRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.ResultSetResponse)
  ))
_sym_db.RegisterMessage(ResultSetResponse)

ExecuteResponse = _reflection.GeneratedProtocolMessageType('ExecuteResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTERESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.ExecuteResponse)
  ))
_sym_db.RegisterMessage(ExecuteResponse)

PrepareResponse = _reflection.GeneratedProtocolMessageType('PrepareResponse', (_message.Message,), dict(
  DESCRIPTOR = _PREPARERESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.PrepareResponse)
  ))
_sym_db.RegisterMessage(PrepareResponse)

FetchResponse = _reflection.GeneratedProtocolMessageType('FetchResponse', (_message.Message,), dict(
  DESCRIPTOR = _FETCHRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.FetchResponse)
  ))
_sym_db.RegisterMessage(FetchResponse)

CreateStatementResponse = _reflection.GeneratedProtocolMessageType('CreateStatementResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTATEMENTRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.CreateStatementResponse)
  ))
_sym_db.RegisterMessage(CreateStatementResponse)

CloseStatementResponse = _reflection.GeneratedProtocolMessageType('CloseStatementResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLOSESTATEMENTRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.CloseStatementResponse)
  ))
_sym_db.RegisterMessage(CloseStatementResponse)

OpenConnectionResponse = _reflection.GeneratedProtocolMessageType('OpenConnectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _OPENCONNECTIONRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.OpenConnectionResponse)
  ))
_sym_db.RegisterMessage(OpenConnectionResponse)

CloseConnectionResponse = _reflection.GeneratedProtocolMessageType('CloseConnectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLOSECONNECTIONRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.CloseConnectionResponse)
  ))
_sym_db.RegisterMessage(CloseConnectionResponse)

ConnectionSyncResponse = _reflection.GeneratedProtocolMessageType('ConnectionSyncResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTIONSYNCRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.ConnectionSyncResponse)
  ))
_sym_db.RegisterMessage(ConnectionSyncResponse)

DatabasePropertyElement = _reflection.GeneratedProtocolMessageType('DatabasePropertyElement', (_message.Message,), dict(
  DESCRIPTOR = _DATABASEPROPERTYELEMENT,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.DatabasePropertyElement)
  ))
_sym_db.RegisterMessage(DatabasePropertyElement)

DatabasePropertyResponse = _reflection.GeneratedProtocolMessageType('DatabasePropertyResponse', (_message.Message,), dict(
  DESCRIPTOR = _DATABASEPROPERTYRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.DatabasePropertyResponse)
  ))
_sym_db.RegisterMessage(DatabasePropertyResponse)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)

SyncResultsResponse = _reflection.GeneratedProtocolMessageType('SyncResultsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SYNCRESULTSRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.SyncResultsResponse)
  ))
_sym_db.RegisterMessage(SyncResultsResponse)

RpcMetadata = _reflection.GeneratedProtocolMessageType('RpcMetadata', (_message.Message,), dict(
  DESCRIPTOR = _RPCMETADATA,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.RpcMetadata)
  ))
_sym_db.RegisterMessage(RpcMetadata)

CommitResponse = _reflection.GeneratedProtocolMessageType('CommitResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMMITRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.CommitResponse)
  ))
_sym_db.RegisterMessage(CommitResponse)

RollbackResponse = _reflection.GeneratedProtocolMessageType('RollbackResponse', (_message.Message,), dict(
  DESCRIPTOR = _ROLLBACKRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.RollbackResponse)
  ))
_sym_db.RegisterMessage(RollbackResponse)

ExecuteBatchResponse = _reflection.GeneratedProtocolMessageType('ExecuteBatchResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEBATCHRESPONSE,
  __module__ = 'pyphoenix.responses_pb2'
  # @@protoc_insertion_point(class_scope:pyphoenix.ExecuteBatchResponse)
  ))
_sym_db.RegisterMessage(ExecuteBatchResponse)


# @@protoc_insertion_point(module_scope)
