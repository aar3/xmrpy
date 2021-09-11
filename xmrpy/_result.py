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

from xmrpy._core import DataClass
from xmrpy.t import List, Dict, Any

__all__ = [
    "CreateAccountResult",
    "CreateAddressResult",
    "MakeIntegratedAddressResult",
    "CreateAddressResult",
    "CheckReserveProofResult",
    "GetTransferByTxId",
    "GetReserveProofResult",
    "SignResult",
    "StopWalletResult",
    "GetAttributeResult",
    "SetTxNotesResult",
    "CheckTxKeyResult",
    "GetAccountsResult",
    "RescanBlockchainResult",
    "GetTransfersResult",
    "SplitIntegratedAddressResult",
    "GetTxNotesResult",
    "VerifyResult",
    "GetAccountTagsResult",
    "GetBulkPaymentsResult",
    "GetAddressIndexResult",
    "CheckSpendProofResult",
    "GetTxKeyResult",
    "GetBalanceResult",
    "GetHeightResult",
    "GetPaymentsResult",
    "GetLanguagesResult",
    "LabelAccountResult",
    "IncomingTransfersResult",
    "SetAttributeResult",
    "LabelAddressResult",
    "SetAccountTagDescriptionResult",
    "TagAccountsResult",
    "SweepAllResult",
    "TransferResult",
    "TransferSplitResult",
    "UntagAccountsResult",
    "SignTransferResult",
    "SubmitTransferResult",
    "SweepSingleResult",
    "RelayTxResult",
    "SweepDustResult",
    "StoreResult",
    "QueryKeyResult",
    "ValidateAddressResult",
    "GetVersionResult",
    "GetTxProofResult",
    "CheckTxProofResult",
    "GetSpendProofResult",
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


class SubmitTransferResult(DataClass):
    tx_hash_list: List[str]


class SweepDustResult(DataClass):
    tx_hash_list: List[str]
    tx_key_list: List[str]
    amount_list: List[int]
    fee_list: List[int]
    tx_blob_list: List[str]
    tx_metadata_list: List[str]
    multisig_txset: str
    unsigned_txset: str


class SweepAllResult(DataClass):
    tx_hash_list: List[str]
    tx_key_list: List[str]
    amount_list: List[int]
    fee_list: List[int]
    tx_blob_list: List[str]
    tx_metadata_list: List[str]
    unsigned_txset: str


class SweepSingleResult(DataClass):
    tx_hash_list: List[str]
    tx_key_list: List[str]
    amount_list: List[int]
    fee_list: List[int]
    tx_blob_list: List[str]
    tx_metadata_list: List[str]
    multisig_txset: str
    unsigned_txset: str


class RelayTxResult(DataClass):
    tx_hash: str


class StoreResult(DataClass):
    pass


class _Payment(DataClass):
    payment_id: str
    tx_hash: str
    amount: int
    block_height: int
    unlock_time: int
    subaddr_index: List[Dict[str, str]]
    address: str


class GetPaymentsResult(DataClass):
    payments: List[_Payment]


class GetBulkPaymentsResult(DataClass):
    payments: List[_Payment]


class _Transfer(DataClass):
    amount: int
    global_index: int
    key_image: str
    spent: bool
    subaddr_index: int
    tx_hash: str
    tx_size: int


class IncomingTransfersResult(DataClass):
    transfers: List[_Transfer]


class QueryKeyResult(DataClass):
    key: str


class MakeIntegratedAddressResult(DataClass):
    integrated_address: str
    payment_id: str


class SplitIntegratedAddressResult(DataClass):
    is_subaddress: bool
    payment_id: str
    standard_address: str


class StopWalletResult(DataClass):
    pass


class RescanBlockchainResult(DataClass):
    pass


class SetTxNotesResult(DataClass):
    pass


class GetTxNotesResult(DataClass):
    notes: List[str]


class SetAttributeResult(DataClass):
    pass


class GetAttributeResult(DataClass):
    value: str


class GetTxKeyResult(DataClass):
    tx_key: str


class CheckTxKeyResult(DataClass):
    confirmations: int
    in_pool: bool
    recevied: bool


class GetTxProofResult(DataClass):
    signature: str


class CheckTxProofResult(DataClass):
    confirmations: int
    good: bool
    in_pool: bool
    received: int


class GetSpendProofResult(DataClass):
    signature: str


class CheckSpendProofResult(DataClass):
    good: bool


class GetReserveProofResult(DataClass):
    signature: str


class CheckReserveProofResult(DataClass):
    good: bool
    spent: int
    total: int


_SubaddrIndex = Dict[str, int]


class _FullTransfer(DataClass):
    address: str
    amount: int
    confirmations: int
    double_spend_seen: int
    fee: int
    height: int
    note: str
    payment_id: str
    subaddr_index: _SubaddrIndex
    suggested_confirmations_threshold: int
    timestamp: int
    txid: str
    type: str
    unlock_time: int


class GetTransfersResult(DataClass):
    # in: List[_FullTransfer]
    out: List[_FullTransfer]
    pending: List[_FullTransfer]
    failed: List[_FullTransfer]
    pool: List[_FullTransfer]

    @property
    def in_(self) -> List[_FullTransfer]:
        t: List[_FullTransfer] = self.__dict__["in"]
        return t


class GetTransferByTxId(DataClass):
    tranfer: _FullTransfer


class SignResult(DataClass):
    signature: str


class VerifyResult(DataClass):
    good: bool
    old: bool
    signature_type: str
    version: int


# ---------


class GetVersionResult(DataClass):
    version: int
