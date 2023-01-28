# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import zksnark_pb2 as api_dot_zksnark__pb2


class TronZksnarkStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CheckZksnarkProof = channel.unary_unary(
                '/protocol.TronZksnark/CheckZksnarkProof',
                request_serializer=api_dot_zksnark__pb2.ZksnarkRequest.SerializeToString,
                response_deserializer=api_dot_zksnark__pb2.ZksnarkResponse.FromString,
                )


class TronZksnarkServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CheckZksnarkProof(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TronZksnarkServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CheckZksnarkProof': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckZksnarkProof,
                    request_deserializer=api_dot_zksnark__pb2.ZksnarkRequest.FromString,
                    response_serializer=api_dot_zksnark__pb2.ZksnarkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'protocol.TronZksnark', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TronZksnark(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CheckZksnarkProof(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/protocol.TronZksnark/CheckZksnarkProof',
            api_dot_zksnark__pb2.ZksnarkRequest.SerializeToString,
            api_dot_zksnark__pb2.ZksnarkResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)