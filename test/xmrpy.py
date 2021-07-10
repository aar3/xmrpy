import string
import random
import pytest
from xmrpy import WalletClient
from xmrpy.config import Config, config


test_config = Config(
    DIGEST_USER_NAME="ralston",
    DIGEST_USER_PASSWD="password",
    DAEMON_RPC_ADDR="127.0.0.1:18081",
    WALLET_RPC_ADDR="127.0.0.1:18083",
)


TEST_ADDR = "4BHuCEqKApGDcMw1tdWfMnb1JQLjvzikFH1jH5At6RkgavSA4hHr4h19qw1MMH1KXrTo8aZRLKBC14vg45qmuDMrSFPbUSk"


class TestUtils:
    @staticmethod
    def random_str(n: int = 10):
        chars = string.ascii_letters + string.digits
        return "".join([chars[random.randint(0, len(chars) - 1)] for _ in range(n)])


class TestWalletClient:
    def setup(self):
        headers = {"Content-Type": "application/json"}
        # pylint: disable=attribute-defined-outside-init
        self.client = WalletClient(config, headers=headers).auth()

    @pytest.mark.asyncio
    async def test_rpcmethod_get_languages(self):
        response = await self.client.get_languages()
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_get_balance(self):
        response = await self.client.get_balance()
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_get_address_index(self):
        response = await self.client.get_address_index(TEST_ADDR)
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_create_address(self):
        response = await self.client.create_address(account_index=0, label="test")
        print(response.as_dict())
        assert not response.is_err()

        assert isinstance(response.result.address, str)
        assert isinstance(response.result.address_index, int)
        assert response.result.address in response.result.addresses
        assert response.result.address_index in response.result.address_indices

    @pytest.mark.asyncio
    async def test_rpcmethod_label_address(self):
        response = await self.client.label_address(major_index=0, minor_index=0, label="Foo")
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_validate_address(self):
        response = await self.client.validate_address(TEST_ADDR)
        print(response.as_dict())
        assert not response.is_err()

        assert response.result.valid
        assert not response.result.integrated
        assert not response.result.subaddress
        assert response.result.nettype == "mainnet"
        assert not response.result.openalias_address

    @pytest.mark.asyncio
    async def test_rpcmethod_get_accounts(self):
        response = await self.client.get_accounts()
        print(response.as_dict())
        assert not response.is_err()

        assert isinstance(response.result.subaddress_accounts, list)
        assert len(response.result.subaddress_accounts) >= 1

    @pytest.mark.asyncio
    async def test_rpcmethod_create_account(self):
        label = TestUtils.random_str()
        response = await self.client.create_account(label)
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.account_index, int)
        assert isinstance(response.result.address, str)

        response = await self.client.validate_address(response.result.address)
        assert response.result.valid

    @pytest.mark.asyncio
    async def test_rpcmethod_label_account(self):
        response = await self.client.label_account(0, "some-label")
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_tag_accounts(self):
        response = await self.client.tag_accounts("foo-tag", accounts=[0])
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip("FIXME: Not working")
    async def test_rpcmethod_get_account_tags(self):
        # IMPORTANT: depends on the tag created in test_rpcmethod_tag_accounts
        response = await self.client.get_account_tags()
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.accounts, list)
        assert len(response.result.accounts) >= 1

    @pytest.mark.asyncio
    async def test_rpcmethod_untag_accounts(self):
        response = await self.client.untag_accounts([0])
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip(reason="FIXME: Not working")
    async def test_rpcmethod_set_account_tag_description(self):
        account_response = await self.client.create_account("miso-soup")
        _ = await self.client.tag_accounts("miso-soup", accounts=[account_response.result.account_index])
        response = await self.client.set_account_tag_description("miso-soup", "Some fake description")

        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod_get_height(self):
        response = await self.client.get_height()
        print(response.as_dict())

        assert not response.is_err()
        assert response.result.height > 0

    @pytest.mark.skip(reason="FIXME: This is a live test and requires a multi test wallet setup")
    async def test_rpcmethod_transfer(self):
        pass

    @pytest.mark.skip(reason="FIXME: This is a live test and requires a multi test wallet setup")
    async def test_rpcmethod_transfer_split(self):
        pass

    @pytest.mark.skip(reason="FIXME: Requires a properly functioning .transfer_split() method")
    async def test_rpcmethod_sign_transfer(self):
        pass
