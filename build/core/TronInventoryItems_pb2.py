# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/TronInventoryItems.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/TronInventoryItems.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=b'\n\017org.tron.protosB\022TronInventoryItemsZ)github.com/tronprotocol/grpc-gateway/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x63ore/TronInventoryItems.proto\x12\x08protocol\"-\n\x0eInventoryItems\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05items\x18\x02 \x03(\x0c\x42P\n\x0forg.tron.protosB\x12TronInventoryItemsZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3'
)




_INVENTORYITEMS = _descriptor.Descriptor(
  name='InventoryItems',
  full_name='protocol.InventoryItems',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.InventoryItems.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='protocol.InventoryItems.items', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['InventoryItems'] = _INVENTORYITEMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InventoryItems = _reflection.GeneratedProtocolMessageType('InventoryItems', (_message.Message,), {
  'DESCRIPTOR' : _INVENTORYITEMS,
  '__module__' : 'core.TronInventoryItems_pb2'
  # @@protoc_insertion_point(class_scope:protocol.InventoryItems)
  })
_sym_db.RegisterMessage(InventoryItems)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
