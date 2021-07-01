from .common import BaseClient, traderrpc
from .errors import handle_rpc_errors


class PoolClient(BaseClient):
    @handle_rpc_errors
    def get_info(self):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.GetInfoRequest()
        response = self._trader_stub.GetInfo(request)
        return response

    @handle_rpc_errors
    def get_lsat_tokens(self):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.TokensRequest()
        response = self._trader_stub.GetLsatTokens(request)
        return response

    @handle_rpc_errors
    def init_account(self, **kwargs):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.InitAccountRequest(**kwargs)
        response = self._trader_stub.InitAccount(request)
        return response

    @handle_rpc_errors
    def auction_fee(self):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.AuctionFeeRequest()
        response = self._trader_stub.AuctionFee(request)
        return response

    @handle_rpc_errors
    def quote_account(self, account_value, conf_target):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.QuoteAccountRequest(
            account_value=account_value, conf_target=conf_target
        )
        response = self._trader_stub.QuoteAccount(request)
        return response

    @handle_rpc_errors
    def quote_order(
        self,
        amt,
        rate_fixed,
        lease_duration_blocks,
        max_batch_fee_rate_sat_per_kw,
        min_units_match,
    ):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.QuoteOrderRequest(
            amt=amt,
            rate_fixed=rate_fixed,
            lease_duration_blocks=lease_duration_blocks,
            max_batch_fee_rate_sat_per_kw=max_batch_fee_rate_sat_per_kw,
            min_units_match=min_units_match,
        )
        response = self._trader_stub.QuoteOrder(request)
        return response

    @handle_rpc_errors
    def next_batch_info(self):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.NextBatchInfoRequest()
        response = self._trader_stub.NextBatchInfo(request)
        return response

    @handle_rpc_errors
    def node_ratings(self, node_pubkeys=[]):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.NodeRatingRequest(node_pubkeys=node_pubkeys)
        response = self._trader_stub.NodeRatings(request)
        return response

    @handle_rpc_errors
    def batch_snapshots(self, start_batch_id, num_batches_back):
        """Unlock encrypted wallet at lnd startup"""
        request = traderrpc.BatchSnapshotsRequest(
            start_batch_id=start_batch_id, num_batches_back=num_batches_back
        )
        response = self._trader_stub.BatchSnapshots(request)
        return response
