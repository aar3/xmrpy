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

# pylint: disable=unused-import
import enum
import json
from typing import (
    Dict,
    TypeVar,
    Any,
    Union,
    Callable,
    Optional,
    List,
    Mapping,
    Generic,
)

__all__ = ["Headers", "TransferType"]

T = TypeVar("T")

Prim = Union[bool, int, str]


class Headers(Dict[str, str]):
    pass


class TransferType(enum.Enum):
    all = "all"
    available = "available"
    unavailable = "unavailable"


class DataClass:
    def __init__(self, data: Mapping[str, Optional[Any]], **kwargs: Dict[str, Optional[Any]]):
        if data:
            if isinstance(data, str):
                as_dict: Dict[str, Any] = json.loads(data)
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
        from xmrpy._utils import dump_dict

        return dump_dict(self.__dict__)

    def _inject_props(self, data: Dict[str, Any]):
        for key, value in data.items():
            self.__dict__[key] = DataClass(value) if isinstance(value, dict) else value

    def __contains__(self, key: str) -> bool:
        return key in self.__dict__

    def items(self):
        return self.__dict__.items()


class RpcError(DataClass):
    code: int
    message: str


class RpcResponse(DataClass, Generic[T]):
    error: RpcError
    result: T
    id: str
    jsonrpc: str

    def is_err(self) -> bool:
        return self.__dict__.get("error") is not None

    def err_details(self) -> Optional[str]:
        if self.is_err():
            m: str = self.error.message
            return m
        return None

    def as_dict(self) -> Dict[str, Prim]:
        from xmrpy._utils import dump_dict

        return dump_dict(self.__dict__)
