from xmrpy._core import DataClass
from xmrpy.t import List, Dict, Any

# NOTE: Keep these in sorted order
__all__ = [
    "CreateAccountResult",
    "CreateAddressResult",
    "CreateAddressResult",
    "GetAccountsResult",
    "GetAccountTagsResult",
    "GetAddressIndexResult",
    "GetBalanceResult",
    "GetHeightResult",
    "GetLanguagesResult",
    "LabelAccountResult",
    "LabelAddressResult",
    "SetAccountTagDescriptionResult",
    "TagAccountsResult",
    "TransferResult",
    "TransferSplitResult",
    "UntagAccountsResult",
    "SignTransferResult",
    "ValidateAddressResult",
]


class GetLanguagesResult(DataClass):
    languages: List[str]
    languages_local: List[str]


class GetBalanceResult(DataClass):
    balance = int
    multisig_import_needed = bool
    peer_subaddress = List[Dict[str, str]]
    unlocked_balance = int


class _Index(DataClass):
    major: int
    minor: int


class GetAddressIndexResult(DataClass):
    index: _Index


class CreateAddressResult(DataClass):
    address: str
    address_index: int
    address_indices: List[int]
    addresses: List[str]


class LabelAddressResult(DataClass):
    label: str


class ValidateAddressResult(DataClass):
    valid: bool
    integrated: bool
    subaddress: bool
    nettype: str
    openalias_address: bool


class _SubaddressAccount(DataClass):
    account_index: int
    balance: int
    base_address: str
    label: str
    unlocked_balance: str


class GetAccountsResult(DataClass):
    subaddress_accounts: List[_SubaddressAccount]
    total_balance: int
    total_unlocked_balance: int


class CreateAccountResult(DataClass):
    account_index: int
    address: str


class LabelAccountResult(DataClass):
    pass


class _AccountTag:
    tag: str
    label: str
    accounts: List[int]


class GetAccountTagsResult(DataClass):
    account_tags: List[_AccountTag]


class TagAccountsResult(DataClass):
    pass


class UntagAccountsResult(DataClass):
    pass


class SetAccountTagDescriptionResult(DataClass):
    pass


class GetHeightResult(DataClass):
    height: int


class TransferResult(DataClass):
    amount: int
    fee: int
    multisig_txset: List[Any]
    tx_blob: str
    tx_hash: str
    tx_key: str
    tx_metadata: str
    unsigned_txset: str


class TransferSplitResult(DataClass):
    tx_hash_list: List[str]
    tx_key_list: List[str]
    amount_list: List[int]
    fee_list: List[int]
    tx_blob_list: List[str]
    tx_metadata_list: List[str]
    multisig_txset: List[str]
    unsigned_txset: List[str]


class SignTransferResult(DataClass):
    signed_txset: str
    tx_hash_list: List[str]
    tx_raw_list: List[str]
