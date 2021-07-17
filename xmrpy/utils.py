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

import re
import json
from xmrpy.t import Any, Dict, Prim


def is_simple_type(value: Any) -> bool:
    return any(
        [
            isinstance(value, bytes),
            isinstance(value, str),
            isinstance(value, int),
            isinstance(value, list),
            isinstance(value, dict),
            value is None,
        ]
    )


def strip_chars(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9:._ ]+", "", s)


def config_file_to_config(p: str):

    from xmrpy.config import Config

    options = {}
    data = None
    with open(p, "r") as file:
        data = json.load(file)

    for optname, item in data.items():
        if isinstance(item, dict):
            for key, value in item.items():
                options[key.upper()] = value
        else:
            options[optname.upper()] = item

    return Config(**options)


def dump_dict(data: Dict[str, Any]) -> Dict[str, Prim]:
    inner = {}
    for key, value in data.items():
        if not is_simple_type(value):
            value = value.as_dict()
        inner[key] = value
    return inner
