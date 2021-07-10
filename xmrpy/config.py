import os
from xmrpy.t import Dict
from xmrpy.utils import config_file_to_config


class Config:

    DAEMON_RPC_ADDR: str = "127.0.0.1:18081"
    WALLET_RPC_ADDR: str = "127.0.0.1:18083"

    DIGEST_USER_NAME: str
    DIGEST_USER_PASSWD: str

    def __init__(self, **kwargs: Dict[str, str]):
        self.__dict__.update(kwargs)


p = os.path.join(os.path.dirname(os.path.relpath(__file__)), "xmrpy.json")
config = config_file_to_config(p)
