import re
import json
from xmrpy.t import Any, Dict, List, Tuple, Mapping


def is_simple_type(value: Any) -> bool:
    return any(
        [
            isinstance(value, bytes),
            isinstance(value, str),
            isinstance(value, int),
            isinstance(value, dict),
            value is None,
        ]
    )


def strip_chars(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9:._ ]+", "", s)


def conf_to_config(p: str):

    from xmrpy.config import Config

    options = {}
    data = None
    with open(p, "r") as file:
        data = json.load(file)

    for _, item in data.items():
        for key, value in item.items():
            options[key.upper()] = value

    return Config(**options)
