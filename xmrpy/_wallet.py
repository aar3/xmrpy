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

from xmrpy.t import Dict, List, Optional, Prim, Generic, T, Any
from xmrpy._core import RpcError
from xmrpy._http import HttpClient, Headers
from xmrpy.utils import dump_dict
from xmrpy.config import Config, config
from xmrpy.const import TransferType
from xmrpy._result import *


class _WalletRpcResponse(Generic[T]):
    error: Optional[RpcError]

    def __init__(self, result: T, data: Dict[str, str]):
        self.result = result
        self.id = data["id"]
        self.jsonrpc = data["jsonrpc"]

    def is_err(self) -> bool:
        return "error" in self.__dict__ and self.__dict__["error"] is not None

    def err_details(self) -> Optional[str]:
        if self.error:
            return self.error.message
        return None

    def as_dict(self) -> Dict[str, Prim]:
        return dump_dict(self.__dict__)


class Client:
    def __init__(self, conf: Optional[Config] = None, headers: Optional[Headers] = None):
        self._config = conf or config
        self._http = HttpClient(headers, timeout=self._config.HTTP_READ_TIMEOUT)
        self.url = "http://" + self._config.WALLET_RPC_ADDR + "/json_rpc"

    def auth(self):
        self._http.set_digest_auth(self._config.DIGEST_USER_NAME, self._config.DIGEST_USER_PASSWD)
        return self

    async def get_languages(self) -> _WalletRpcResponse[GetLanguagesResult]:
        data = self._attach_default_params({"method": "get_languages"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetLanguagesResult(rpcmsg["result"]), data)

    async def get_balance(
        self, account_index: int = 0, address_indices: List[int] = [0]
    ) -> _WalletRpcResponse[GetBalanceResult]:
        data = self._attach_default_params(
            {
                "method": "get_balance",
                "params": {"account_index": account_index, "address_indices": address_indices},  # type: ignore
            }
        )

        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetBalanceResult(rpcmsg["result"]), data)

    async def get_address_index(self, address: str) -> _WalletRpcResponse[GetAddressIndexResult]:
        data = self._attach_default_params({"method": "get_address_index", "params": {"address": address}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetAddressIndexResult(rpcmsg["result"]), data)

    async def create_address(
        self, account_index: int, label: Optional[str] = None
    ) -> _WalletRpcResponse[CreateAddressResult]:
        data = self._attach_default_params(
            {
                "method": "create_address",
                "params": {"account_index": account_index, "label": label},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(CreateAddressResult(rpcmsg["result"]), data)

    async def label_address(
        self, major_index: int, minor_index: int, label: str
    ) -> _WalletRpcResponse[LabelAddressResult]:
        data = self._attach_default_params(
            {
                "method": "label_address",
                "params": {
                    "index": {"major": major_index, "minor": minor_index},
                    "label": label,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(LabelAddressResult(rpcmsg["result"]), data)

    async def validate_address(
        self,
        address: str,
        any_net_type: bool = False,
        allow_openalias: bool = False,
    ) -> _WalletRpcResponse[ValidateAddressResult]:
        data = self._attach_default_params(
            {
                "method": "validate_address",
                "params": {
                    "address": address,
                    "any_net_type": any_net_type,
                    "allow_openalias": allow_openalias,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(ValidateAddressResult(rpcmsg["result"]), data)

    async def get_accounts(self, tag: Optional[str] = None) -> _WalletRpcResponse[GetAccountsResult]:
        data = self._attach_default_params(
            {
                "method": "get_accounts",
                "params": {
                    "tag": tag,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetAccountsResult(rpcmsg["result"]), data)

    async def create_account(self, label: Optional[str] = None) -> _WalletRpcResponse[CreateAccountResult]:
        data = self._attach_default_params(
            {
                "method": "create_account",
                "params": {
                    "label": label,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(CreateAccountResult(rpcmsg["result"]), data)

    async def label_account(self, account_index: int, label: str) -> _WalletRpcResponse[LabelAccountResult]:
        data = self._attach_default_params(
            {
                "method": "label_account",
                "params": {
                    "account_index": account_index,
                    "label": label,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(LabelAccountResult(rpcmsg["result"]), data)

    async def tag_accounts(self, tag: str, accounts: List[int]) -> _WalletRpcResponse[TagAccountsResult]:
        data = self._attach_default_params(
            {
                "method": "tag_accounts",
                "params": {"tags": tag, "accounts": accounts},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(TagAccountsResult(rpcmsg["result"]), data)

    async def get_account_tags(self) -> _WalletRpcResponse[GetAccountTagsResult]:
        data = self._attach_default_params(
            (
                {
                    "method": "get_account_tags",
                    "params": "",
                }
            )
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetAccountTagsResult(rpcmsg["result"]), data)

    async def untag_accounts(self, accounts: List[int]) -> _WalletRpcResponse[UntagAccountsResult]:
        data = self._attach_default_params({"method": "untag_accounts", "params": {"accounts": accounts}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(UntagAccountsResult(rpcmsg["result"]), data)

    async def set_account_tag_description(
        self, tag: str, description: str
    ) -> _WalletRpcResponse[SetAccountTagDescriptionResult]:
        data = self._attach_default_params(
            {
                "method": "set_account_tag_description",
                "params": {"tag": tag, "description": description},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SetAccountTagDescriptionResult(rpcmsg["result"]), data)

    async def get_height(self) -> _WalletRpcResponse[GetHeightResult]:
        data = self._attach_default_params({"method": "get_height"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetHeightResult(rpcmsg["result"]), data)

    async def transfer(
        self,
        destinations: List[Dict[str, int]],
        account_index: int = 0,
        subaddress_indices: List[int] = [],
        priority: int = 0,
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_key: bool = True,
        do_not_relay: bool = False,
        get_tx_hex: bool = False,
        get_tx_metadata: bool = False,
    ) -> _WalletRpcResponse[TransferResult]:
        data = self._attach_default_params(
            {
                "method": "transfer",
                "params": {
                    "destinations": destinations,
                    "account_index": account_index,
                    "subaddress_indices": subaddress_indices,
                    "priority": priority,
                    "mixin": mixin,
                    "ring_size": ring_size,
                    "unlock_time": unlock_time,
                    "get_tx_key": get_tx_key,
                    "do_not_relay": do_not_relay,
                    "get_tx_hex": get_tx_hex,
                    "get_tx_metadata": get_tx_metadata,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(TransferResult(rpcmsg["result"]), data)

    async def transfer_split(
        self,
        destinations: List[Dict[str, int]],
        account_index: int = 0,
        subaddress_indices: List[int] = [],
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_keys: bool = True,
        priority: int = 0,
        do_not_relay: bool = False,
        get_tx_hex: bool = False,
        new_algorithm: bool = False,
        get_tx_metadata: bool = False,
    ):
        data = self._attach_default_params(
            {
                "method": "transfer_split",
                "params": {
                    "destinations": destinations,
                    "account_index": account_index,
                    "subaddress_indices": subaddress_indices,
                    "priority": priority,
                    "mixin": mixin,
                    "ring_size": ring_size,
                    "unlock_time": unlock_time,
                    "get_tx_key": get_tx_keys,
                    "do_not_relay": do_not_relay,
                    "get_tx_hex": get_tx_hex,
                    "new_algorithm": new_algorithm,
                    "get_tx_metadata": get_tx_metadata,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(TransferSplitResult(rpcmsg["result"]), data)

    async def sign_transfer(
        self, unsigned_txset: str, export_raw: bool = False
    ) -> _WalletRpcResponse[SignTransferResult]:
        data = self._attach_default_params(
            {
                "method": "sign_transfer",
                "params": {
                    "unsigned_tx_set": unsigned_txset,
                    "export_raw": export_raw,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SignTransferResult(rpcmsg["result"]), data)

    async def submit_transfer(self, tx_data_hex: str) -> _WalletRpcResponse[SubmitTransferResult]:
        data = self._attach_default_params(
            {
                "method": "submit_transfer",
                "params": {"tx_data_hex": tx_data_hex},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SubmitTransferResult(rpcmsg["result"]), data)

    async def sweep_dust(
        self,
        get_tx_keys: bool = True,
        do_not_relay: bool = False,
        get_tx_hex: bool = False,
        get_tx_metadata: bool = False,
    ):
        data = self._attach_default_params(
            {
                "method": "sweep_dust",
                "params": {
                    "get_tx_keys": get_tx_keys,
                    "do_not_relay": do_not_relay,
                    "get_tx_hex": get_tx_hex,
                    "get_tx_metadata": get_tx_metadata,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SweepDustResult(rpcmsg["result"]), data)

    async def sweep_all(
        self,
        address: str,
        account_index: int,
        subaddr_indices: List[int] = [0],
        priority: int = 0,
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_keys: Optional[bool] = True,
        below_amount: Optional[int] = None,
        do_not_relay: bool = False,
        get_tx_hex: bool = False,
        get_tx_metadata: bool = False,
    ) -> _WalletRpcResponse[SweepAllResult]:
        data = self._attach_default_params(
            {
                "methods": "sweep_all",
                "params": {
                    "address": address,
                    "account_index": account_index,
                    "subaddr_indices": subaddr_indices,
                    "priority": priority,
                    "mixin": mixin,
                    "ring_size": ring_size,
                    "unlock_time": unlock_time,
                    "get_tx_keys": get_tx_keys,
                    "below_amount": below_amount,
                    "do_not_relay": do_not_relay,
                    "get_tx_hex": get_tx_hex,
                    "get_tx_metadata": get_tx_metadata,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SweepAllResult(rpcmsg["result"]), data)

    async def sweep_single(
        self,
        address: str,
        account_index: int,
        key_image: str,
        subaddr_indices: List[int] = [0],
        priority: int = 0,
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_keys: Optional[bool] = True,
        below_amount: Optional[int] = None,
        do_not_relay: bool = False,
        get_tx_hex: bool = False,
        get_tx_metadata: bool = False,
    ) -> _WalletRpcResponse[SweepAllResult]:
        data = self._attach_default_params(
            {
                "methods": "sweep_all",
                "params": {
                    "address": address,
                    "account_index": account_index,
                    "subaddr_indices": subaddr_indices,
                    "priority": priority,
                    "mixin": mixin,
                    "ring_size": ring_size,
                    "key_image": key_image,
                    "unlock_time": unlock_time,
                    "get_tx_keys": get_tx_keys,
                    "below_amount": below_amount,
                    "do_not_relay": do_not_relay,
                    "get_tx_hex": get_tx_hex,
                    "get_tx_metadata": get_tx_metadata,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SweepAllResult(rpcmsg["result"]), data)

    async def relay_tx(self, tx_hex: str) -> _WalletRpcResponse[RelayTxResult]:
        data = self._attach_default_params({"method": "relay_tx", "params": {"hex": tx_hex}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(RelayTxResult(rpcmsg["result"]), data)

    async def store(self) -> _WalletRpcResponse[StoreResult]:
        data = self._attach_default_params({"method": "store"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(StoreResult(rpcmsg["result"]), data)

    async def get_payments(self, payment_id: str) -> _WalletRpcResponse[GetPaymentsResult]:
        data = self._attach_default_params({"method": "get_payments", "params": {"payment_id": payment_id}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetPaymentsResult(rpcmsg["result"]), data)

    async def get_bulk_payments(
        self, payment_ids: List[str], min_block_height: int
    ) -> _WalletRpcResponse[GetBulkPaymentsResult]:
        data = self._attach_default_params(
            {
                "method": "get_bulk_payments",
                "params": {"payment_ids": payment_ids, "min_block_height": min_block_height},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetBulkPaymentsResult(rpcmsg["result"]), data)

    async def incoming_transfers(
        self, transfer_type: TransferType, account_index: int = 0, subaddr_indices: Optional[List[int]] = None
    ) -> _WalletRpcResponse[IncomingTransfersResult]:
        data = self._attach_default_params(
            {
                "method": "incoming_transfers",
                "params": {
                    "transfer_type": transfer_type.value,
                    "account_index": account_index,
                    "subaddr_indices": subaddr_indices,
                },
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(IncomingTransfersResult(rpcmsg["result"]), data)

    async def query_key(self, key_type: str) -> _WalletRpcResponse[QueryKeyResult]:
        data = self._attach_default_params({"method": "query_key", "params": {"key_type": key_type}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(QueryKeyResult(rpcmsg["result"]), data)

    async def make_integrated_address(
        self, standard_address: Optional[str] = None, payment_id: Optional[str] = None
    ) -> _WalletRpcResponse[MakeIntegratedAddressResult]:
        data = self._attach_default_params(
            {
                "method": "make_integrated_address",
                "params": {"standard_address": standard_address, "payment_id": payment_id},
            }
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(MakeIntegratedAddressResult(rpcmsg["result"]), data)

    async def split_integrated_address(
        self, integrated_address: str
    ) -> _WalletRpcResponse[SplitIntegratedAddressResult]:
        data = self._attach_default_params(
            {"method": "split_integrated_address", "params": {"integrated_address": integrated_address}}
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SplitIntegratedAddressResult(rpcmsg["result"]), data)

    async def stop_wallet(self) -> _WalletRpcResponse[StopWalletResult]:
        data = self._attach_default_params({"method": "stop_wallet"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(StopWalletResult(rpcmsg["result"]), data)

    async def rescan_blockchain(self) -> _WalletRpcResponse[RescanBlockchainResult]:
        data = self._attach_default_params({"method": "rescan_blockchain"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(RescanBlockchainResult(rpcmsg["result"]), data)

    async def set_tx_notes(self, txids: List[str], notes: List[str]) -> _WalletRpcResponse[SetTxNotesResult]:
        data = self._attach_default_params({"method": "set_tx_notes", "params": {"txids": txids, "notes": notes}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SetTxNotesResult(rpcmsg["result"]), data)

    async def get_tx_notes(self, txids: List[str]) -> _WalletRpcResponse[GetTxNotesResult]:
        data = self._attach_default_params({"method": "get_tx_notes", "params": {"txids": txids}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetTxNotesResult(rpcmsg["result"]), data)

    async def set_attribute(self, key: str, value: str) -> _WalletRpcResponse[SetAttributeResult]:
        data = self._attach_default_params({"method": "set_attribute", "params": {"key": key, "value": value}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(SetAttributeResult(rpcmsg["result"]), data)

    async def get_attribute(self, key: str) -> _WalletRpcResponse[GetAttributeResult]:
        data = self._attach_default_params({"method": "get_attribute", "params": {"key": key}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetAttributeResult(rpcmsg["result"]), data)

    async def get_tx_key(self, txid: str) -> _WalletRpcResponse[GetTxKeyResult]:
        data = self._attach_default_params({"method": "get_tx_key", "params": {"txid": txid}})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetTxKeyResult(rpcmsg["result"]), data)

    async def check_tx_key(self, txid: str, tx_key: str, address: str) -> _WalletRpcResponse[CheckTxKeyResult]:
        data = self._attach_default_params(
            {"method": "check_tx_key", "params": {"txid": txid, "tx_key": tx_key, "address": address}}
        )
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(CheckTxKeyResult(rpcmsg["result"]), data)

    # -------------

    async def get_version(self) -> _WalletRpcResponse[GetVersionResult]:
        data = self._attach_default_params({"method": "get_version"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _WalletRpcResponse(GetVersionResult(rpcmsg["result"]), data)

    def _attach_default_params(self, data: Dict[str, Any]) -> Dict[str, str]:
        payload = {"id": "0", "jsonrpc": "2.0"}
        payload.update(data)
        return payload
