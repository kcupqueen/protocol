# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/contract/market_contract.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core/contract/market_contract.proto',
  package='protocol',
  syntax='proto3',
  serialized_options=b'\n\030org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#core/contract/market_contract.proto\x12\x08protocol\"\x96\x01\n\x17MarketSellAssetContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x15\n\rsell_token_id\x18\x02 \x01(\x0c\x12\x1b\n\x13sell_token_quantity\x18\x03 \x01(\x03\x12\x14\n\x0c\x62uy_token_id\x18\x04 \x01(\x0c\x12\x1a\n\x12\x62uy_token_quantity\x18\x05 \x01(\x03\"D\n\x19MarketCancelOrderContract\x12\x15\n\rowner_address\x18\x01 \x01(\x0c\x12\x10\n\x08order_id\x18\x02 \x01(\x0c\x42\x45\n\x18org.tron.protos.contractZ)github.com/tronprotocol/grpc-gateway/coreb\x06proto3'
)




_MARKETSELLASSETCONTRACT = _descriptor.Descriptor(
  name='MarketSellAssetContract',
  full_name='protocol.MarketSellAssetContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.MarketSellAssetContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sell_token_id', full_name='protocol.MarketSellAssetContract.sell_token_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sell_token_quantity', full_name='protocol.MarketSellAssetContract.sell_token_quantity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buy_token_id', full_name='protocol.MarketSellAssetContract.buy_token_id', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='buy_token_quantity', full_name='protocol.MarketSellAssetContract.buy_token_quantity', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=50,
  serialized_end=200,
)


_MARKETCANCELORDERCONTRACT = _descriptor.Descriptor(
  name='MarketCancelOrderContract',
  full_name='protocol.MarketCancelOrderContract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='owner_address', full_name='protocol.MarketCancelOrderContract.owner_address', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='protocol.MarketCancelOrderContract.order_id', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=202,
  serialized_end=270,
)

DESCRIPTOR.message_types_by_name['MarketSellAssetContract'] = _MARKETSELLASSETCONTRACT
DESCRIPTOR.message_types_by_name['MarketCancelOrderContract'] = _MARKETCANCELORDERCONTRACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MarketSellAssetContract = _reflection.GeneratedProtocolMessageType('MarketSellAssetContract', (_message.Message,), {
  'DESCRIPTOR' : _MARKETSELLASSETCONTRACT,
  '__module__' : 'core.contract.market_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.MarketSellAssetContract)
  })
_sym_db.RegisterMessage(MarketSellAssetContract)

MarketCancelOrderContract = _reflection.GeneratedProtocolMessageType('MarketCancelOrderContract', (_message.Message,), {
  'DESCRIPTOR' : _MARKETCANCELORDERCONTRACT,
  '__module__' : 'core.contract.market_contract_pb2'
  # @@protoc_insertion_point(class_scope:protocol.MarketCancelOrderContract)
  })
_sym_db.RegisterMessage(MarketCancelOrderContract)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
