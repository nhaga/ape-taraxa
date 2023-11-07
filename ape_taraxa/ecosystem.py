from ape.api.config import PluginConfig
from ape_ethereum.ecosystem import Ethereum, NetworkConfig
from ape_ethereum.transactions import TransactionType

NETWORKS = {
    "mainnet": (841, 841),
    "testnet": (842, 842),
}


taraxa_config = NetworkConfig(
    default_provider="taraxa",
    default_transaction_type=TransactionType.STATIC,
    gas_limit=1_000_000,
)


class TaraxaConfig(PluginConfig):
    mainnet: NetworkConfig = taraxa_config
    testnet: NetworkConfig = taraxa_config
    local: NetworkConfig = NetworkConfig(
        default_transaction_type=TransactionType.STATIC, default_provider="test"
    )


class Taraxa(Ethereum):
    @property
    def config(self) -> TaraxaConfig:
        return self.config_manager.get_config("taraxa")
