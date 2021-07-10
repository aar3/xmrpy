from xmrpy.t import Dict, List, Optional, Prim, Generic, T, Any
from xmrpy._core import RpcError
from xmrpy._http import HttpClient, Headers
from xmrpy.utils import dump_dict
from xmrpy.config import Config, config
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
        self._http = HttpClient(headers)
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
        any_net_type: Optional[bool] = False,
        allow_openalias: Optional[bool] = False,
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
        account_index: Optional[int] = 0,
        subaddress_indices: Optional[List[int]] = [],
        priority: int = 0,
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_key: Optional[bool] = True,
        do_not_relay: Optional[bool] = False,
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
        account_index: Optional[int] = 0,
        subaddress_indices: Optional[List[int]] = [],
        mixin: int = 0,
        ring_size: int = 7,
        unlock_time: int = 0,
        get_tx_keys: Optional[bool] = True,
        priority: int = 0,
        do_not_relay: Optional[bool] = False,
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
        self, unsigned_txset: str, export_raw: Optional[bool] = False
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

    def _attach_default_params(self, data: Dict[str, Any]) -> Dict[str, str]:
        payload = {"id": "0", "jsonrpc": "2.0"}
        payload.update(data)
        return payload
