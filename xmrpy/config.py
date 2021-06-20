class Config:

    DAEMON_RPC_ADDR: str
    WALLET_RPC_ADDR: str

    DIGEST_USER_NAME: str
    DIGEST_USER_PASSWD: str

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
