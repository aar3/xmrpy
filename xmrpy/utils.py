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

    for _, item in data.items():
        for key, value in item.items():
            options[key.upper()] = value

    return Config(**options)


def dump_dict(data: Dict[str, Any]) -> Dict[str, Prim]:
    inner = {}
    for key, value in data.items():
        if not is_simple_type(value):
            value = value.as_dict()
        inner[key] = value
    return inner
