import json
from xmrpy.t import Dict, Prim, Any, Optional, Union, Mapping
from xmrpy.utils import is_simple_type


class Error(Exception):
    pass


class DTO:
    def __init__(self, data: Union[str, Mapping[str, Prim]], **kwargs: Dict[str, Prim]):
        if data:
            if isinstance(data, str):
                as_dict: Dict[str, Prim] = json.loads(data)
                self._inject_props(as_dict)
            elif isinstance(data, dict):
                self._inject_props(data)
            else:
                raise TypeError("Illegal DTO value '{}'".format(type(data)))
        elif kwargs:
            self._inject_props(kwargs)

    def serialize(self) -> bytes:
        return json.dumps(self.as_dict()).encode()

    def as_dict(self) -> Dict[str, Prim]:
        inner = {}
        for key, value in self.__dict__.items():
            if not is_simple_type(value):
                value = value.as_dict()
            inner[key] = value
        return inner

    def _inject_props(self, data: Dict[str, Any]):
        self.__dict__.update(data)

    def __contains__(self, key: str) -> bool:
        return key in self.__dict__


class RpcError(DTO):
    code: int
    message: str


class BaseResponse(DTO):
    id: str
    jsonrpc: str
    error: Optional[RpcError]

    def is_err(self) -> bool:
        return "error" in self

    def err_details(self) -> Optional[str]:
        if self.error:
            return self.error.message
        return None
