import enum
from xmrpy.t import Dict, List, Optional, Any, Prim, Union, Callable
from xmrpy._core import DTO, BaseResponse
from xmrpy._http import HttpClient, Headers
from xmrpy.config import Config
from xmrpy.utils import is_simple_type


class _GetLanguagesResult(DTO):
    languages: List[str]
    languages_local: List[str]


class _GetBalanceResult(DTO):
    balance = int
    multisig_import_needed = bool
    peer_subaddress = List[Dict[str, str]]
    unlocked_balance = int


_ResultDTO = Union[
    _GetLanguagesResult,
    _GetBalanceResult,
]


class _Result:
    GetLanguages = _GetLanguagesResult
    GetBalance = _GetBalanceResult


class _Response(BaseResponse):
    result: _ResultDTO

    def __init__(self, result: _ResultDTO):
        self.result = result


class Client:
    def __init__(self, config: Config, headers: Headers):
        self._config = config
        self._http = HttpClient(headers)
        self.url = "http://" + config.WALLET_RPC_ADDR + "/json_rpc"

    def auth(self):
        self._http.set_digest_auth(self._config.DIGEST_USER_NAME, self._config.DIGEST_USER_PASSWD)
        return self

    async def get_languages(self) -> _Response:
        data = self._prep_payload({"method": "get_languages"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _Response(_Result.GetLanguages(rpcmsg))

    async def get_balance(self, account_index: int = 0, address_indices: List[int] = [0]) -> _Response:
        data = self._prep_payload(
            {
                "method": "get_balance",
                "params": {"account_index": account_index, "address_indices": address_indices},  # type: ignore
            }
        )

        rpcmsg = await self._http.post(self.url, data=data)
        return _Response(_Result.GetBalance(rpcmsg))

    def _prep_payload(self, data: Dict[str, str]) -> Dict[str, str]:
        payload = {"id": "0", "jsonrpc": "2.0"}
        payload.update(data)
        return payload
