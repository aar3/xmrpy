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
