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

import os
from xmrpy.t import Dict
from xmrpy.utils import config_file_to_config


class Config:

    DAEMON_RPC_ADDR: str = "127.0.0.1:18081"
    WALLET_RPC_ADDR: str = "127.0.0.1:18083"

    DIGEST_USER_NAME: str
    DIGEST_USER_PASSWD: str

    HTTP_READ_TIMEOUT: int = 3

    def __init__(self, **kwargs: Dict[str, str]):
        self.__dict__.update(kwargs)


p = os.path.join(os.path.dirname(os.path.relpath(__file__)), "xmrpy.json")
config = config_file_to_config(p)
