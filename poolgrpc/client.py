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
