import json
import httpx
from xmrpy.t import Optional, Dict, Any


class Headers(Dict[str, str]):
    pass


class HttpClient:
    def __init__(self, headers: Optional[Dict[str, str]] = None):
        self._headers = headers
        self._httpx = httpx.AsyncClient()
        self._auth: httpx.DigestAuth

    def _handle_response(self, response: httpx.Response):
        if response.status_code != 200:
            return {
                "result": None,
                "error": {"code": response.status_code, "message": response.text},
                "id": "0",
                "jsonrpc": "2.0",
            }
        return response.json()

    async def post(self, url: str, data: Optional[Dict[str, Any]]):
        compact = json.dumps(data)
        response = await self._httpx.post(url, headers=self._headers, data=compact, auth=self._auth)  # type: ignore
        return self._handle_response(response)

    def set_digest_auth(self, user: str, passwd: str):
        self._auth = httpx.DigestAuth(user, passwd)
