import pytest
from xmrpy import WalletClient
from xmrpy.config import Config, config
from xmrpy.utils import is_simple_type


test_config = Config(
    DIGEST_USER_NAME="ralston",
    DIGEST_USER_PASSWD="password",
    DAEMON_RPC_ADDR="127.0.0.1:18081",
    WALLET_RPC_ADDR="127.0.0.1:18083",
)


class TestUtils:
    def test_is_simple_type_returns_true_for_dict(self):
        assert is_simple_type({})


class TestWalletClient:
    def setup(self):
        headers = {"Content-Type": "application/json"}
        # pylint: disable=attribute-defined-outside-init
        self.client = WalletClient(config, headers=headers).auth()

    @pytest.mark.asyncio
    async def test_rpcmethod_get_languages(self):
        result = await self.client.get_languages()
        print(result.as_dict())
        assert not result.is_err()
