# Copyright 2021 Rashad Alston

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
# EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
# USE OR OTHER DEALINGS IN THE SOFTWARE.

import string
import random
import pytest
from xmrpy import Wallet
from xmrpy._config import Config, config
from xmrpy._utils import TransferType


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


class TestWallet:
    def setup(self):
        headers = {"Content-Type": "application/json"}
        # pylint: disable=attribute-defined-outside-init
        self.client = Wallet(config, headers=headers).auth()

    @pytest.mark.asyncio
    async def test_rpcmethod__get_languages(self):
        response = await self.client.get_languages()
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__get_balance(self):
        response = await self.client.get_balance()
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__get_address_index(self):
        response = await self.client.get_address_index(TEST_ADDR)
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__create_address(self):
        response = await self.client.create_address(account_index=0, label="test")
        print(response.as_dict())
        assert not response.is_err()

        assert isinstance(response.result.address, str)
        assert isinstance(response.result.address_index, int)
        assert response.result.address in response.result.addresses
        assert response.result.address_index in response.result.address_indices

    @pytest.mark.asyncio
    async def test_rpcmethod__label_address(self):
        response = await self.client.label_address(major_index=0, minor_index=0, label="Foo")
        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__validate_address(self):
        response = await self.client.validate_address(TEST_ADDR)
        print(response.as_dict())
        assert not response.is_err()

        assert response.result.valid
        assert not response.result.integrated
        assert not response.result.subaddress
        assert response.result.nettype == "mainnet"
        assert not response.result.openalias_address

    @pytest.mark.asyncio
    async def test_rpcmethod__get_accounts(self):
        response = await self.client.get_accounts()
        print(response.as_dict())
        assert not response.is_err()

        assert isinstance(response.result.subaddress_accounts, list)
        assert len(response.result.subaddress_accounts) >= 1

    @pytest.mark.asyncio
    async def test_rpcmethod__create_account(self):
        label = TestUtils.random_str()
        response = await self.client.create_account(label)
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.account_index, int)
        assert isinstance(response.result.address, str)

        response = await self.client.validate_address(response.result.address)
        assert response.result.valid

    @pytest.mark.asyncio
    async def test_rpcmethod__label_account(self):
        response = await self.client.label_account(0, "some-label")
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__tag_accounts(self):
        response = await self.client.tag_accounts("foo-tag", accounts=[0])
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip("FIXME: Not working")
    async def test_rpcmethod__get_account_tags(self):
        # IMPORTANT: depends on the tag created in test_rpcmethod__tag_accounts
        response = await self.client.get_account_tags()
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.accounts, list)
        assert len(response.result.accounts) >= 1

    @pytest.mark.asyncio
    async def test_rpcmethod__untag_accounts(self):
        response = await self.client.untag_accounts([0])
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip(reason="FIXME: Not working")
    async def test_rpcmethod__set_account_tag_description(self):
        account_response = await self.client.create_account("miso-soup")
        _ = await self.client.tag_accounts("miso-soup", accounts=[account_response.result.account_index])
        response = await self.client.set_account_tag_description("miso-soup", "Some fake description")

        print(response.as_dict())
        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__get_height(self):
        response = await self.client.get_height()
        print(response.as_dict())

        assert not response.is_err()
        assert response.result.height > 0

    @pytest.mark.skip(reason="Requires a mulit-wallet set up")
    async def test_rpcmethod__transfer(self):
        pass

    @pytest.mark.skip(reason="Requires a mulit-wallet set up")
    async def test_rpcmethod__transfer_split(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer_split()")
    async def test_rpcmethod__sign_transfer(self):
        pass

    @pytest.mark.skip(reason="Blocked .sign_transfer()")
    async def test_rpcmethod__submit_transfer(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__sweep_dust(self):
        response = await self.client.sweep_dust()
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.xfail(reason="RPC documentation response is -32600 error")
    @pytest.mark.asyncio
    async def test_rpcmethod__sweep_all(self):
        response = await self.client.sweep_all(TEST_ADDR, account_index=0)
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.xfail(reason="RPC documentation response is -32600 error")
    @pytest.mark.asyncio
    async def test_rpcmethod__sweep_single(self):
        response = await self.client.sweep_all(TEST_ADDR, account_index=0)
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__relay_tx(self):
        TEST_HEX = "1c42dcc5672bb09bccf33fb1e9ab4a498af59a6dbd33b3d0cfb289b9e0e25fa5"
        response = await self.client.relay_tx(TEST_HEX)
        print(response.as_dict())

        assert not response.is_err()

        assert isinstance(response.result.tx_hash, str)

    @pytest.mark.skip(reason="What is a payment?")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_payments(self):
        pass

    @pytest.mark.skip(reason="Blocked by .get_payments()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_bulk_payments(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__incoming_transfers(self):
        response = await self.client.incoming_transfers(TransferType.all)
        print(response.as_dict())

        assert not response.is_err()
        # FIXME: This is probably blocked by needed existing transfers
        # assert isinstance(response.result.transfers, list)

    @pytest.mark.asyncio
    async def test_rpcmethod__query_key(self):
        response = await self.client.query_key("view_key")
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.key, str)

    @pytest.mark.asyncio
    async def test_rpcmethod__make_integrated_address(self):
        response = await self.client.make_integrated_address()
        print(response.as_dict())

        assert not response.is_err()

        assert isinstance(response.result.payment_id, str)
        assert isinstance(response.result.integrated_address, str)

    @pytest.mark.asyncio
    async def test_rpcmethod__split_integrated_address(self):
        r = await self.client.make_integrated_address()
        response = await self.client.split_integrated_address(r.result.integrated_address)
        print(response.as_dict())

        assert not response.is_err()

        assert isinstance(response.result.payment_id, str)
        assert isinstance(response.result.standard_address, str)
        assert not response.result.is_subaddress

    @pytest.mark.skip(reason="Works, but will stop the wallet")
    @pytest.mark.asyncio
    async def test_rpcmethod__stop_wallet(self):
        response = await self.client.stop_wallet()
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip(reason="Rescan takes too long for test suite, but works.")
    @pytest.mark.asyncio
    async def test_rpcmethod__rescan_blockchain(self):
        response = await self.client.rescan_blockchain()
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__set_tx_notes(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_tx_notes(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__set_attribute(self):
        response = await self.client.set_attribute("foo", "bar")
        print(response.as_dict())

        assert not response.is_err()

    @pytest.mark.asyncio
    async def test_rpcmethod__get_attribute(self):
        response = await self.client.get_attribute("foo")

        assert not response.is_err()

        assert response.result.value == "bar"

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_tx_key(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__check_tx_key(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_tx_proof(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__check_tx_proof(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_spend_proof(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__check_spend_proof(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_reserve_proof(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    @pytest.mark.asyncio
    async def test_rpcmethod__check_reserve_proof(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__get_transfers(self):
        response = await self.client.get_transfers()
        assert not response.is_err()

        print(response.as_dict())

        # FIXME: still dependent on .transfer()
        # assert isinstance(response.result.in_, list)

    @pytest.mark.skip(reason="Blocked by .get_transfers()")
    @pytest.mark.asyncio
    async def test_rpcmethod__get_transfer_by_tx_id(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__sign(self):
        response = await self.client.sign("Attack at dawn")
        assert not response.is_err()

        print(response.as_dict())
        assert isinstance(response.result.signature, str)

    @pytest.mark.asyncio
    async def test_rpcmethod__verify(self):
        msg = "attack at dawn"
        sig_response = await self.client.sign(msg)
        response = await self.client.verify(msg, TEST_ADDR, sig_response.result.signature)

        assert not response.is_err()

        print(response.as_dict())

        assert response.result.good

    @pytest.mark.asyncio
    async def test_rpcmethod__export_outputs(self):
        response = await self.client.export_outputs()
        assert not response.is_err()

        print(response.as_dict())

        assert isinstance(response.result.outputs_data_hex, str)

    @pytest.mark.skip(reason="Blocked by unknown dependency")
    @pytest.mark.asyncio
    async def test_rpcmethod__import_outputs(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__export_key_images(self):
        response = await self.client.export_key_images()
        assert not response.is_err()

        print(response.as_dict())

    @pytest.mark.skip(reason="Blocked by unknown dependency")
    @pytest.mark.asyncio
    async def test_rpcmethod__import_key_images(self):
        pass

    @pytest.mark.asyncio
    async def test_rpcmethod__make_uri(self):
        response = await self.client.make_uri(TEST_ADDR)
        assert not response.is_err()

        print(response.as_dict())

        assert isinstance(response.result.uri, str)

    @pytest.mark.asyncio
    async def test_rpcmethod__parse_uri(self):
        uri_resp = await self.client.make_uri(TEST_ADDR)

        response = await self.client.parse_uri(uri_resp.result.uri)
        assert not response.is_err()

        print(response.as_dict())

        assert isinstance(response.result.uri.address, str)

    @pytest.mark.asyncio
    async def test_rpcmethod__get_address_book(self):
        response = await self.client.get_address_book([1])
        assert not response.is_err()

        print(response.as_dict())
        assert isinstance(response.result.entries, list)

    # ---------

    @pytest.mark.asyncio
    async def test_rpcmethod__get_version(self):
        response = await self.client.get_version()
        print(response.as_dict())

        assert not response.is_err()
        assert isinstance(response.result.version, int)
