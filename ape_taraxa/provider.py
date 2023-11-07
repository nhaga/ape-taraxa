from ape.api import ProviderAPI, Web3Provider
from ape.api.transactions import TransactionAPI
from ape.exceptions import TransactionError
from web3 import HTTPProvider, Web3


class TaraxaProvider(Web3Provider, ProviderAPI):
    @property
    def uri(self) -> str:
        rpcs = {
            841: "https://rpc.mainnet.taraxa.io",
            842: "https://rpc.testnet.taraxa.io",
        }
        return rpcs.get(self.chain_id)

    def connect(self):
        self._web3 = Web3(HTTPProvider(self.uri))

    def disconnect(self):
        self._web3 = None

    def prepare_transaction(self, txn: TransactionAPI) -> TransactionAPI:
        # NOTE: Use "expected value" for Chain ID, so if it doesn't match actual, we raise
        txn.chain_id = self.network.chain_id

        txn.gas_price = 500_000_000_000

        from ape_ethereum.transactions import StaticFeeTransaction, TransactionType

        txn_type = TransactionType(txn.type)
        if (
            txn_type == TransactionType.STATIC
            and isinstance(txn, StaticFeeTransaction)
            and txn.gas_price is None
        ):
            txn.gas_price = self.gas_price
        elif txn_type == TransactionType.DYNAMIC:
            if txn.max_priority_fee is None:
                txn.max_priority_fee = self.priority_fee

            if txn.max_fee is None:
                txn.max_fee = self.base_fee + txn.max_priority_fee
            # else: Assume user specified the correct amount or txn will fail and waste gas

        if txn.gas_limit is None:
            txn.gas_limit = self.estimate_gas_cost(txn)

        if txn.required_confirmations is None:
            txn.required_confirmations = self.network.required_confirmations
        elif not isinstance(txn.required_confirmations, int) or txn.required_confirmations < 0:
            raise TransactionError("'required_confirmations' must be a positive integer.")

        return txn
