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
from xmrpy.t import Dict, Prim, Any, Union, Mapping
from xmrpy.utils import dump_dict


class DataClass:
    def __init__(self, data: Union[str, Mapping[str, Prim]], **kwargs: Dict[str, Prim]):
        if data:
            if isinstance(data, str):
                as_dict: Dict[str, Prim] = json.loads(data)
                self._inject_props(as_dict)
            elif isinstance(data, dict):
                self._inject_props(data)
            else:
                raise TypeError("Illegal DataClass value '{}'".format(type(data)))

        elif kwargs:
            self._inject_props(kwargs)

    def serialize(self) -> bytes:
        return json.dumps(self.as_dict()).encode()

    def as_dict(self) -> Dict[str, Prim]:
        return dump_dict(self.__dict__)

    def _inject_props(self, data: Dict[str, Any]):
        self.__dict__.update(data)

    def __contains__(self, key: str) -> bool:
        return key in self.__dict__


class RpcError(DataClass):
    code: int
    message: str
