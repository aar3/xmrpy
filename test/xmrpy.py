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
import os
import random
import pytest
from xmrpy import Wallet, atomic_unit_multiplier
from xmrpy._config import Config, config
from xmrpy.t import TransferType


test_config = Config(
    DIGEST_USER_NAME="ralston",
    DIGEST_USER_PASSWORD="password",
    DAEMON_RPC_ADDR="127.0.0.1:18081",
    WALLET_RPC_ADDR="127.0.0.1:18083",
    LOG_LEVEL="DEBUG",
    LOG_FILE="xmrpy.test.log",
)

TEST_ADDR = "4BHuCEqKApGDcMw1tdWfMnb1JQLjvzikFH1jH5At6RkgavSA4hHr4h19qw1MMH1KXrTo8aZRLKBC14vg45qmuDMrSFPbUSk"
TEST_RECV_ADDR = "83Gwvm9JV6TQvzjfLeRxnaUPMF6cHaK4cVtcrLmZQmnfWEr5hDsoJuXPVYy7yP9f1rXxSTRt8FJBK7MKfUGDBsyc5RKAn1c"
MIN_TRANSFER_AMOUNT = 0.0000000001 * atomic_unit_multiplier

PREV_TRANSFER_RESPONSE = {
    "id": "0",
    "jsonrpc": "2.0",
    "result": {
        "amount": 100,
        "fee": 8270000,
        "multisig_txset": "",
        "spent_key_images": {"key_images": ["fda4094cf7225f6ac4e19c14b56ed192c321a4e011f58443dd4c18aeac35175a"]},
        "tx_blob": "02000102000bacd7e20fb2bfea02eeff0bd1b90cb4c101eadf028af402ed1dfe518810b80efda4094cf7225f6ac4e19c14b56ed192c321a4e011f58443dd4c18aeac35175a020002f6e71c1d0243febf01eb5e9a7c418938533b411dc8942200dcd19ed4459d86a200025e629271e8462462d6ec0997872610982352dd5644a92cad87fe59ff65a2f19a2c01d3652e386d74152d9fccbed789602d2fcb34cdc8e2d43172d024c7a3169453590209011fb08f44c230f32805b0e1f8030fc8eb321ee29c91bf73566f3b93398d94ce4ffb8d1ebfbf89b3863e4a29e8aa6223cb68c86c7e688e119c053e02bccc448a2c18f1373cd9816dc316cfba82698fcca1c418bd8737ea970252789b1404016d31f1b54ef01f1f009cc4b13ec96a8d1f7d98603db7d3aa531190bdee593d0cd0310319bc77317b889fe27164d16d08de6fc96ce78434d9c4d156d3edd0a0fed3f431ce1053c255c5eabce43346c31bb0b6bc9f8f4c8ed703f2a47b426e7c646ada0e3b763e4026201b13c6e9589c5af863d325c1cd9a5746f8d079a0ef9a4049ba7a4f212aad6a5089bdfd54187145284c3a2cca80ea35846e25d3e2d4c804ef5db38eb1a7a4e86e9211587bad29b37ca409ecaa42282d6dc09f5bb4d7ab0b07f09a86d1190b1f6a0605519accbceff6be18b7a33338235df3ee41db1052735e87846f9709f00b698b4a787eb2eab3e5c4e7923f41bc757e35dd6655b4d4aea8740d760f41f3dd936913f415343ba278743ac6f23665714600ec0293db088c7af86135be78a1b31f3ab9904cc02ec2308c1f711a931bf4f024e5e48af91affb7570fdec2be152857aca6fa21f0479f0d65447720737c8b62d1f68a724801562d17ec0e059ae6ce43b104bd0b7d5bd23ca32031c80aa7449f4cc80feca97b0eaee8953941409fcf440904277929fd3f110a16b62c3ea116be03ec7f369527b6a807ca94cb0e920227afd37fdd916e0d2fbb321b284f0921cc9668fc9b71f7f645d03fa0d2d0c786f4dfdd548a6da1baa9589ec4a89f929b99a0d9077738c32c8df33e51c73619a42df9a9d148c1c0b4d044ce2d4730312755b41b9efe3c6ce2e8a0a14c10ceb6bbbcf922e6f1cf5c35bd678cda2f71658d4e973946cba72fc696ab0d59c543a41450a0852c4c1c6c800959d5dbb89c84c8d39ed30fd0c849e18035b938444039bc030d062cafe128aabea8c648fb5f2cc95d5ac11dea5218604984efddaecbe8c48b05e7d535ba566256cfee87ead45315adfeff7e02eb9c07230dc17b4befc830371bdc24caea50c0a159a52bb3e03fce2750c2a483336e10730a7f7148166bb0d9d212480558ab5bcd0df5c74fa03a50bb612cd01b2c47c7010d39bb66644285eb7ad13135b9f9c3f8dce322450bf636b76615c24feae89138036c4aefad4d986e2da6a77204879a7ccd3ab1be420757b084b0603fb38f91b30fbf2cbfd05c469878351736c3b28ac66660d29353caa3003306c0ddb0951fdb0eda7d7beaa8473b380c6913836c746bb564965a31ff6f373c9b639cb8c4c7b904cd90987f4fcaf83cc1ddbb12871ca7d61171de53849b230d221d0fc31fb8110d5430276d875f3624adda2d57a3cc1620b87269a2221c6f7e279a0f405a64d4047fbab72074076ec616677e7de0e1e1a4df056e76f9a27266b8c06a7dbf4b18048a6d2d65cf4bb9d3ceadf2a0de09dbff09abcc4757680224197c719d4c3fbb0474f3d0272b17259a465d04e55aa7f0efbad695e8f75a90456bcd509af837de08f586caff38a1bb71342dd3556fc75dc261faa21a5dcb03356d990966eab7bf04afcdc34d3b4659dfacd7472b0ff4b96469dbace0f2e89d441142a9ceb8e9340247b2aa2bfc3f28a32e0a506ae574f6459eb68067ad999a85b641d19e9fe1600d01041bb9e7c1c62444251969556eb25084644bd025f1af2de0bebd98973b810c3d95c016e212bbb3a963bc46f6de9f55705262991955dbf1bd934bcd0cc198414dffc6093569f9539844c46f2a68108bc143795ff42e6cb8e062596b0de8d5d6",
        "tx_hash": "5885d365f50564cf92cccd4542287af16951c590eff7fc7fe1daf88eb480d65e",
        "tx_key": "4e3aec0d967f8e5e2d17a5be59edb4174bd1552f131b50ce716dacc58727cb02",
        "tx_metadata": "02000102000bacd7e20fb2bfea02eeff0bd1b90cb4c101eadf028af402ed1dfe518810b80efda4094cf7225f6ac4e19c14b56ed192c321a4e011f58443dd4c18aeac35175a020002f6e71c1d0243febf01eb5e9a7c418938533b411dc8942200dcd19ed4459d86a200025e629271e8462462d6ec0997872610982352dd5644a92cad87fe59ff65a2f19a2c01d3652e386d74152d9fccbed789602d2fcb34cdc8e2d43172d024c7a3169453590209011fb08f44c230f32805b0e1f8030fc8eb321ee29c91bf73566f3b93398d94ce4ffb8d1ebfbf89b3863e4a29e8aa6223cb68c86c7e688e119c053e02bccc448a2c18f1373cd9816dc316cfba82698fcca1c418bd8737ea970252789b1404016d31f1b54ef01f1f009cc4b13ec96a8d1f7d98603db7d3aa531190bdee593d0cd0310319bc77317b889fe27164d16d08de6fc96ce78434d9c4d156d3edd0a0fed3f431ce1053c255c5eabce43346c31bb0b6bc9f8f4c8ed703f2a47b426e7c646ada0e3b763e4026201b13c6e9589c5af863d325c1cd9a5746f8d079a0ef9a4049ba7a4f212aad6a5089bdfd54187145284c3a2cca80ea35846e25d3e2d4c804ef5db38eb1a7a4e86e9211587bad29b37ca409ecaa42282d6dc09f5bb4d7ab0b07f09a86d1190b1f6a0605519accbceff6be18b7a33338235df3ee41db1052735e87846f9709f00b698b4a787eb2eab3e5c4e7923f41bc757e35dd6655b4d4aea8740d760f41f3dd936913f415343ba278743ac6f23665714600ec0293db088c7af86135be78a1b31f3ab9904cc02ec2308c1f711a931bf4f024e5e48af91affb7570fdec2be152857aca6fa21f0479f0d65447720737c8b62d1f68a724801562d17ec0e059ae6ce43b104bd0b7d5bd23ca32031c80aa7449f4cc80feca97b0eaee8953941409fcf440904277929fd3f110a16b62c3ea116be03ec7f369527b6a807ca94cb0e920227afd37fdd916e0d2fbb321b284f0921cc9668fc9b71f7f645d03fa0d2d0c786f4dfdd548a6da1baa9589ec4a89f929b99a0d9077738c32c8df33e51c73619a42df9a9d148c1c0b4d044ce2d4730312755b41b9efe3c6ce2e8a0a14c10ceb6bbbcf922e6f1cf5c35bd678cda2f71658d4e973946cba72fc696ab0d59c543a41450a0852c4c1c6c800959d5dbb89c84c8d39ed30fd0c849e18035b938444039bc030d062cafe128aabea8c648fb5f2cc95d5ac11dea5218604984efddaecbe8c48b05e7d535ba566256cfee87ead45315adfeff7e02eb9c07230dc17b4befc830371bdc24caea50c0a159a52bb3e03fce2750c2a483336e10730a7f7148166bb0d9d212480558ab5bcd0df5c74fa03a50bb612cd01b2c47c7010d39bb66644285eb7ad13135b9f9c3f8dce322450bf636b76615c24feae89138036c4aefad4d986e2da6a77204879a7ccd3ab1be420757b084b0603fb38f91b30fbf2cbfd05c469878351736c3b28ac66660d29353caa3003306c0ddb0951fdb0eda7d7beaa8473b380c6913836c746bb564965a31ff6f373c9b639cb8c4c7b904cd90987f4fcaf83cc1ddbb12871ca7d61171de53849b230d221d0fc31fb8110d5430276d875f3624adda2d57a3cc1620b87269a2221c6f7e279a0f405a64d4047fbab72074076ec616677e7de0e1e1a4df056e76f9a27266b8c06a7dbf4b18048a6d2d65cf4bb9d3ceadf2a0de09dbff09abcc4757680224197c719d4c3fbb0474f3d0272b17259a465d04e55aa7f0efbad695e8f75a90456bcd509af837de08f586caff38a1bb71342dd3556fc75dc261faa21a5dcb03356d990966eab7bf04afcdc34d3b4659dfacd7472b0ff4b96469dbace0f2e89d441142a9ceb8e9340247b2aa2bfc3f28a32e0a506ae574f6459eb68067ad999a85b641d19e9fe1600d01041bb9e7c1c62444251969556eb25084644bd025f1af2de0bebd98973b810c3d95c016e212bbb3a963bc46f6de9f55705262991955dbf1bd934bcd0cc198414dffc6093569f9539844c46f2a68108bc143795ff42e6cb8e062596b0de8d5d60000000000000000b0307e00000000000000ecb99dc5a201ff24f841884aa94b636737e7b53cb5cb4dbbcaae4b19485fbb9e6d41236fddcacd51d280ccd46434df675c4650e805a032ef9594a5b9661777ec1ed8888cc9df00000100433c666461343039346366373232356636616334653139633134623536656431393263333231613465303131663538343433646434633138616561633335313735613e204e3aec0d967f8e5e2d17a5be59edb4174bd1552f131b50ce716dacc58727cb0200015f38334777766d394a56365451767a6a664c6552786e6155504d46366348614b3463567463724c6d5a516d6e66574572356844736f4a7558505659793779503966317258785354527438464a424b374d4b665547444273796335524b416e31636415b33aec726f148f12e6faec4ccc7fa3b9e6cca3f7c0a1acb8c9e17d0d59e0aece932a55b76a1a8678f22af2b97fa9b912a9188c7d083a25f766f316ceae4b270100010b02acd7e20f9c7dab71cb3656bed2bedb1c43f5bab81294f0675d9875e4b6c1fdac3f72a8c704d8570def869224c8cf33b97213ed804a2a5ff495f401acb2aae28cc72be49302de96cd12dba691a13f6c36e60773cf976ff1c5719e2495fb61778fbfd19e406911f7eca9e9d6209704107145a87a7ef4419c9d777b6b1920a819713248e0c34a25a80f7602cc96d912f138b8045f3bab4444f0391247f90a99504060323ecae1967cba0ddb5a63cd82dcd4059f39d251121a85c1e4f6f68f810ceef99450f89a012c94a8827ba9b447029dd0e51224f7453d2deb222b667e6930749ed07962a8fb13e4780a51e92b4351355a28d2eae8ede5b3cf7c809adcdda3fa0eabe39d15ee32d1959dc71883552093d080da02d191e71218bf7e40c46ef923f96e65738634a08c51dba67a7acf8fee76f981cbda7a9ce8fc8a4b56f6449d9d67b3000f32eb8443947e830e520daee9159a0db2ff81924502bbf1e91206f1b5548431edd670fce1d25f02e8e3e728542cc3da4d8d6750c6e7d9b7cec270eae207b87eb7918bd69e4f716b87974086f4bab224765405e36f32930b422702c5e5ec12f1a0f68508a4a15176ee277d4f2e95a16a7e4fb32800cf9a4e5e12852c6090cbad3e127da65a038683a8974aef37f98a3197fd2caf2a78e416aaf94fbf76588502b283ed12e06d25e7f24e9bf1a4a97a7e025256494382a771f869f086fc90327c2c4f1c1d938d4d3c24ced976e48e8907233f44050219fa22073ff33eb98c3ddf2fe9ee0102b0d5ed12036aa9ea893f7cf6b5cb5e26538c5c6747ad4a08b85ca40b5748fa4a2dfc26881a577ec17d22f05f6aa747afb81eaacbc15af828d54e86d2e882d5c84951edea02b8e5ed12e92dbf625f147ec9559e52bfcd91584fd4ee8dd2ce1f87491b9ad7493af0c6074b739347fe0ad5f32998d6353b7aa293e026bb190d8f5a8e3502f938999bd8ff02f0f3ed1238877f9649fce85add00a3cb444377c29b40607d5000e3dab6be341b63a4e8d973e2307a328f17c1216562e85b25698de78f0d140173a05dc681eaa415e8b2dc0300000000000000693b914e66bdc541f1381616165f5ef77fbfe5c117e40d7a3ad03cbe74171d96000000000000000000008e25290a00000001db906faf8d7d8855d091d2798e8ebd4f1b2ae5504710addf7d7d0db629c38309000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ecb99dc5a201ff24f841884aa94b636737e7b53cb5cb4dbbcaae4b19485fbb9e6d41236fddcacd51d280ccd46434df675c4650e805a032ef9594a5b9661777ec1ed8888cc9df0000025f38334777766d394a56365451767a6a664c6552786e6155504d46366348614b3463567463724c6d5a516d6e66574572356844736f4a7558505659793779503966317258785354527438464a424b374d4b665547444273796335524b416e31636415b33aec726f148f12e6faec4ccc7fa3b9e6cca3f7c0a1acb8c9e17d0d59e0aece932a55b76a1a8678f22af2b97fa9b912a9188c7d083a25f766f316ceae4b27010000ecb99dc5a201ff24f841884aa94b636737e7b53cb5cb4dbbcaae4b19485fbb9e6d41236fddcacd51d280ccd46434df675c4650e805a032ef9594a5b9661777ec1ed8888cc9df000001002c01d3652e386d74152d9fccbed789602d2fcb34cdc8e2d43172d024c7a3169453590209011fb08f44c230f328000000000000000001000303015f38334777766d394a56365451767a6a664c6552786e6155504d46366348614b3463567463724c6d5a516d6e66574572356844736f4a7558505659793779503966317258785354527438464a424b374d4b665547444273796335524b416e31636415b33aec726f148f12e6faec4ccc7fa3b9e6cca3f7c0a1acb8c9e17d0d59e0aece932a55b76a1a8678f22af2b97fa9b912a9188c7d083a25f766f316ceae4b27010000000000010000",
        "unsigned_txset": "",
        "weight": 1455,
    },
    "error": None,
}


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

    @pytest.mark.asyncio
    @pytest.mark.skipif(not os.environ.get("THIRD_PARTY_TESTS"), reason="set THIRD_PARTY_TESTS=1 to test .transfer()")
    async def test_rpcmethod__transfer(self):
        response = await self.client.transfer(
            destinations=[{"amount": MIN_TRANSFER_AMOUNT, "address": TEST_RECV_ADDR}],
            account_index=0,
            get_tx_hex=True,
            get_tx_metadata=True,
        )
        print(response.as_dict())

        assert not response.is_err()
        assert response.result.amount is not None
        assert response.result.fee is not None
        assert isinstance(response.result.tx_key, str)
        assert isinstance(response.result.tx_hash, str)
        assert isinstance(response.result.unsigned_txset, str)

    @pytest.mark.skip(reason="Blocked by .transfer()")
    async def test_rpcmethod__transfer_split(self):
        pass

    @pytest.mark.skip(reason="Blocked by .transfer()")
    async def test_rpcmethod__sign_transfer(self):
        response = await self.sign_transfer(unsigned_txset=PREV_TRANSFER_RESPONSE["result"]["unsigned_txset"], export_raw=True)
        print(response.as_dict())

        assert not response.is_err()

        assert isinstance(response.result.signed_txset, str)
        assert isinstance(response.result.tx_hash_list, list)
        assert isinstance(response.result.tx_raw_list, list)


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
