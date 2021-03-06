# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from poolgrpc.compiled import auctioneer_pb2 as poolgrpc_dot_compiled_dot_auctioneer__pb2


class ChannelAuctioneerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReserveAccount = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/ReserveAccount',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountResponse.FromString,
                )
        self.InitAccount = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/InitAccount',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountResponse.FromString,
                )
        self.ModifyAccount = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/ModifyAccount',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountResponse.FromString,
                )
        self.SubmitOrder = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/SubmitOrder',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderResponse.FromString,
                )
        self.CancelOrder = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/CancelOrder',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderResponse.FromString,
                )
        self.OrderState = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/OrderState',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateResponse.FromString,
                )
        self.SubscribeBatchAuction = channel.stream_stream(
                '/poolrpc.ChannelAuctioneer/SubscribeBatchAuction',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.FromString,
                )
        self.SubscribeSidecar = channel.stream_stream(
                '/poolrpc.ChannelAuctioneer/SubscribeSidecar',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.FromString,
                )
        self.Terms = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/Terms',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsResponse.FromString,
                )
        self.RelevantBatchSnapshot = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/RelevantBatchSnapshot',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatchRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatch.FromString,
                )
        self.BatchSnapshot = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/BatchSnapshot',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotResponse.FromString,
                )
        self.NodeRating = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/NodeRating',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingResponse.FromString,
                )
        self.BatchSnapshots = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/BatchSnapshots',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsResponse.FromString,
                )
        self.MarketInfo = channel.unary_unary(
                '/poolrpc.ChannelAuctioneer/MarketInfo',
                request_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoRequest.SerializeToString,
                response_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoResponse.FromString,
                )


class ChannelAuctioneerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ReserveAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ModifyAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubmitOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OrderState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeBatchAuction(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeSidecar(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Terms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelevantBatchSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchSnapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NodeRating(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchSnapshots(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarketInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChannelAuctioneerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReserveAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.ReserveAccount,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountResponse.SerializeToString,
            ),
            'InitAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.InitAccount,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountResponse.SerializeToString,
            ),
            'ModifyAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.ModifyAccount,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountResponse.SerializeToString,
            ),
            'SubmitOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.SubmitOrder,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderResponse.SerializeToString,
            ),
            'CancelOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOrder,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderResponse.SerializeToString,
            ),
            'OrderState': grpc.unary_unary_rpc_method_handler(
                    servicer.OrderState,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateResponse.SerializeToString,
            ),
            'SubscribeBatchAuction': grpc.stream_stream_rpc_method_handler(
                    servicer.SubscribeBatchAuction,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.SerializeToString,
            ),
            'SubscribeSidecar': grpc.stream_stream_rpc_method_handler(
                    servicer.SubscribeSidecar,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.SerializeToString,
            ),
            'Terms': grpc.unary_unary_rpc_method_handler(
                    servicer.Terms,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsResponse.SerializeToString,
            ),
            'RelevantBatchSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.RelevantBatchSnapshot,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatchRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatch.SerializeToString,
            ),
            'BatchSnapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchSnapshot,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotResponse.SerializeToString,
            ),
            'NodeRating': grpc.unary_unary_rpc_method_handler(
                    servicer.NodeRating,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingResponse.SerializeToString,
            ),
            'BatchSnapshots': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchSnapshots,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsResponse.SerializeToString,
            ),
            'MarketInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.MarketInfo,
                    request_deserializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoRequest.FromString,
                    response_serializer=poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'poolrpc.ChannelAuctioneer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChannelAuctioneer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ReserveAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/ReserveAccount',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ReserveAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/InitAccount',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerInitAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ModifyAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/ModifyAccount',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerModifyAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubmitOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/SubmitOrder',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerSubmitOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/CancelOrder',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerCancelOrderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OrderState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/OrderState',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerOrderStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeBatchAuction(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/poolrpc.ChannelAuctioneer/SubscribeBatchAuction',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeSidecar(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/poolrpc.ChannelAuctioneer/SubscribeSidecar',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ClientAuctionMessage.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerAuctionMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Terms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/Terms',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.TermsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelevantBatchSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/RelevantBatchSnapshot',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatchRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.RelevantBatch.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchSnapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/BatchSnapshot',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NodeRating(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/NodeRating',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.ServerNodeRatingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BatchSnapshots(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/BatchSnapshots',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.BatchSnapshotsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarketInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/poolrpc.ChannelAuctioneer/MarketInfo',
            poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoRequest.SerializeToString,
            poolgrpc_dot_compiled_dot_auctioneer__pb2.MarketInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
