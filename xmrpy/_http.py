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

import json
import httpx
from xmrpy.t import (
    Optional,
    Dict,
    Any,
    Callable,
    RpcError,
    Headers,
    RpcResponse,
)


class HttpClient:
    def __init__(self, headers: Optional[Headers], timeout: int = 3):
        self._headers = headers
        self._httpx = httpx.AsyncClient(timeout=timeout)
        self._auth: httpx.DigestAuth

    async def post(
        self,
        url: str,
        data: Optional[Dict[str, Any]] = None,
        ResultClass: Any = Callable[[Any], Any],
    ):
        compact = json.dumps(data)
        response = await self._httpx.post(url, headers=self._headers, content=compact, auth=self._auth)  # type: ignore
        if response.status_code != 200:
            return RpcResponse(
                {
                    "result": None,
                    "error": RpcError({"code": response.status_code, "message": response.text}),
                    "id": "0",
                    "jsonrpc": "2.0",
                }
            )

        rjson = response.json()
        if not "error" in rjson:
            rjson.update({"result": ResultClass(rjson["result"]), "error": None})
        return RpcResponse(rjson)

    def set_digest_auth(self, user: str, passwd: str):
        self._auth = httpx.DigestAuth(user, passwd)
