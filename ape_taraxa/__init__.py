from ape import plugins
from ape.api import NetworkAPI, create_network_type
from ape.api.networks import LOCAL_NETWORK_NAME
from ape_test import LocalProvider

from .ecosystem import NETWORKS, Taraxa, TaraxaConfig
from .provider import TaraxaProvider


@plugins.register(plugins.Config)
def config_class():
    return TaraxaConfig


@plugins.register(plugins.EcosystemPlugin)
def ecosystems():
    yield Taraxa


@plugins.register(plugins.NetworkPlugin)
def networks():
    for network_name, network_params in NETWORKS.items():
        yield "taraxa", network_name, create_network_type(*network_params)

    yield "taraxa", LOCAL_NETWORK_NAME, NetworkAPI


@plugins.register(plugins.ProviderPlugin)
def providers():
    for network_name in NETWORKS:
        yield "taraxa", network_name, TaraxaProvider

    yield "taraxa", LOCAL_NETWORK_NAME, LocalProvider
