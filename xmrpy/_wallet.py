from xmrpy.t import Dict, List, Optional, Prim, Union, Mapping
from xmrpy._core import DTO, BaseResponse
from xmrpy._http import HttpClient, Headers
from xmrpy.config import Config, config


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

    def __init__(self, result: _ResultDTO, data: Union[str, Mapping[str, Prim]], **kwargs: Dict[str, Prim]):
        self.result = result
        super(_Response, self).__init__(data, **kwargs)


class Client:
    def __init__(self, conf: Optional[Config] = None, headers: Optional[Headers] = None):
        self._config = conf or config
        self._http = HttpClient(headers)
        self.url = "http://" + self._config.WALLET_RPC_ADDR + "/json_rpc"

    def auth(self):
        self._http.set_digest_auth(self._config.DIGEST_USER_NAME, self._config.DIGEST_USER_PASSWD)
        return self

    async def get_languages(self) -> _Response:
        data = self._prep_payload({"method": "get_languages"})
        rpcmsg = await self._http.post(self.url, data=data)
        return _Response(_Result.GetLanguages(rpcmsg), data)

    async def get_balance(self, account_index: int = 0, address_indices: List[int] = [0]) -> _Response:
        data = self._prep_payload(
            {
                "method": "get_balance",
                "params": {"account_index": account_index, "address_indices": address_indices},  # type: ignore
            }
        )

        rpcmsg = await self._http.post(self.url, data=data)
        return _Response(_Result.GetBalance(rpcmsg), data)

    def _prep_payload(self, data: Dict[str, str]) -> Dict[str, str]:
        payload = {"id": "0", "jsonrpc": "2.0"}
        payload.update(data)
        return payload
