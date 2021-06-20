from xmrpy.t import Any


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
