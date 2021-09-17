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

import enum
from xmrpy.t import List, Dict, Any, DataClass


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


class ExportOutputsResult(DataClass):
    outputs_data_hex: str


class ImportOutputsResult(DataClass):
    num_imported: int


class SignedKeyImage(DataClass):
    key_image: str
    signature: str


class ExportKeyImagesResult(DataClass):
    signed_key_images: List[SignedKeyImage]
    offset: int


class ImportKeyImagesResult(DataClass):
    height: int
    spent: int
    unspent: int


class MakeUriResult(DataClass):
    uri: str


class _Uri(DataClass):
    address: str
    amount: int
    payment_id: str
    recipient_name: str
    tx_description: str


class ParseUriResult(DataClass):
    uri: _Uri


class _AddressBookEntry(DataClass):
    address: str
    descrpition: str
    index: int
    payment_id: str


class GetAddressBookResult(DataClass):
    entries: List[_AddressBookEntry]


class AddAddressBookResult(DataClass):
    index: int


class GetVersionResult(DataClass):
    version: int


class EditAddressBookResult(DataClass):
    pass


class DeleteAddressBookResult(DataClass):
    pass


class RefreshResult(DataClass):
    pass


class AutoRefreshResult(DataClass):
    pass


class RescanSpentResult(DataClass):
    pass


class StartMiningResult(DataClass):
    pass


class StopMiningResult(DataClass):
    pass


class CreateWalletResult(DataClass):
    pass


class GenerateFromKeysResult(DataClass):
    address: str
    info: str


class OpenWalletResult(DataClass):
    pass


class RestoreDeterministicWalletResult(DataClass):
    address: str
    info: str
    seed: str
    was_deprecated: bool


class CloseWalletResult(DataClass):
    pass


class ChangeWalletPasswordResult(DataClass):
    pass


class IsMultisigResult(DataClass):
    multisig: bool
    ready: bool
    threshold: int
    total: int


class PrepareMultisigResult(DataClass):
    multisig_info: str


class MakeMultisigResult(DataClass):
    pass


class ExportMultisigInfoResult(DataClass):
    info: str


class ImportMultisigInfoResult(DataClass):
    n_outputs: int


class MultisigInfoResult(DataClass):
    address: str


class FinalizeMultisigResult(DataClass):
    address: str
    multisig_info: str


class SignMultisigResult(DataClass):
    tx_data_hex: str
    tx_hash_list: List[str]


class SubmitMultisigResult(DataClass):
    tx_hash_list: str


class Result(enum.Enum):
    AddAddressBook = AddAddressBookResult
    AutoRefresh = AutoRefreshResult
    ChangeWalletPassword = ChangeWalletPasswordResult
    CheckReserveProof = CheckReserveProofResult
    CheckSpendProof = CheckSpendProofResult
    CheckTxKey = CheckTxKeyResult
    CheckTxProof = CheckTxProofResult
    CloseWallet = CloseWalletResult
    CreateAccount = CreateAccountResult
    CreateAddress = CreateAddressResult
    CreateWallet = CreateWalletResult
    DeleteAddressBook = DeleteAddressBookResult
    EditAddressBook = EditAddressBookResult
    ExportKeyImages = ExportKeyImagesResult
    ExportMultisigInfo = ExportMultisigInfoResult
    ExportOutputs = GetAccountsResult
    FinalizeMultisig = FinalizeMultisigResult
    GenerateFromKeys = GenerateFromKeysResult
    GetAccounts = GetAccountsResult
    GetAccountTags = GetAccountTagsResult
    GetAddressBook = GetAddressBookResult
    GetAddressIndex = GetAddressIndexResult
    GetAttribute = GetAttributeResult
    GetBalance = GetBalanceResult
    GetBulkPayments = GetBulkPaymentsResult
    GetHeight = GetHeightResult
    GetLanguages = GetLanguagesResult
    GetPayments = GetPaymentsResult
    GetReserveProof = GetReserveProofResult
    GetSpendProof = GetSpendProofResult
    GetTransferByTxId = GetTransfersResult
    GetTransfers = GetTransfersResult
    GetTxKey = GetTxKeyResult
    GetTxNotes = GetTxNotesResult
    GetTxProof = GetTxProofResult
    GetVersion = GetVersionResult
    ImportKeyImages = ImportKeyImagesResult
    ImportMultisigInfo = ImportMultisigInfoResult
    ImportOutputs = IncomingTransfersResult
    IncomingTransfers = IncomingTransfersResult
    IsMultisig = IsMultisigResult
    LabelAccount = LabelAccountResult
    LabelAddress = LabelAddressResult
    MakeIntegratedAddress = MakeIntegratedAddressResult
    MakeMultisig = MakeMultisigResult
    MakeUri = MakeUriResult
    MultisigInfo = MultisigInfoResult
    OpenWallet = OpenWalletResult
    ParseUri = ParseUriResult
    PrepareMultisig = PrepareMultisigResult
    QueryKey = QueryKeyResult
    Refresh = RefreshResult
    RelayTx = RelayTxResult
    RescanBlockchain = RescanBlockchainResult
    RescanSpent = RescanSpentResult
    RestoreDeterministicWallet = RestoreDeterministicWalletResult
    SetAccountTagDescription = SetAccountTagDescriptionResult
    SetAttribute = SetAttributeResult
    SetTxNotes = SetTxNotesResult
    Sign = SignResult
    SignedKeyImage = SignedKeyImage
    SignMultisig = SignMultisigResult
    SignTransfer = SignTransferResult
    SplitIntegratedAddress = SplitIntegratedAddressResult
    StartMining = StartMiningResult
    StopMining = StopMiningResult
    StopWallet = StopWalletResult
    Store = StoreResult
    SubmitMultisig = SubmitMultisigResult
    SubmitTransfer = SubmitTransferResult
    SweepAll = SweepAllResult
    SweepDust = SweepDustResult
    SweepSingle = SweepSingleResult
    TagAccounts = TagAccountsResult
    Transfer = TransferResult
    TransferSplit = TransferSplitResult
    UntagAccounts = UntagAccountsResult
    ValidateAddress = ValidateAddressResult
    Verify = VerifyResult
