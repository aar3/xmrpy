# xmrpy

Based on the JSON RPC API available at https://www.getmonero.org/resources/developer-guides/wallet-rpc.html

[A list of community run, publicly accessibly Monero nodes](https://monero.fail/)

![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/aar3/xmrpy/httpx)

![GitHub issues](https://img.shields.io/github/issues/aar3/xmrpy)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/aar3/xmrpy)

## Dependencies
	- A full Monero node
		- `XMRPY_DIR=/xmr/root/directory USER=monero-node-user PASSWORd=password scripts/daemon.bash`
	- A Monero wallet
		- `

<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2d/Monero-Logo.svg/1280px-Monero-Logo.svg.png' height='100'>

✅ = Passing unit test(s)
🚫 = Unit tests TBD

# RPC Methods
- [x] ✅ set_daemon
- [x] ✅ sget_balance
- [x] ✅ sget_address
- [x] ✅ sget_address_index
- [x] ✅ screate_address
- [x] ✅ slabel_address
- [x] ✅ svalidate_address
- [x] ✅ get_accounts
- [x] ✅ create_account
- [x] ✅ label_account
- [x] ✅ get_account_tags
- [x] ✅ tag_accounts
- [x] ✅ untag_accounts
- [x] ✅ set_account_tag_description
- [x] ✅ get_height
- [x] 🚫 transfer
- [x] 🚫 transfer_split
- [x] 🚫 sign_transfer
- [x] 🚫 submit_transfer
- [x] sweep_dust
- [x] sweep_all
- [x] sweep_single
- [x] 🚫 relay_tx
- [x] store
- [x] get_payments
- [x] get_bulk_payments
- [x] 🚫 incoming_transfers
- [x] query_key
- [x] make_integrated_address
- [x] split_integrated_address
- [x] ✅ stop_wallet
- [x] ✅ rescan_blockchain
- [x] 🚫 set_tx_notes
- [x] 🚫 get_tx_notes
- [x] ✅ set_attribute
- [x] ✅ get_attribute
- [x] 🚫 get_tx_key
- [x] 🚫 check_tx_key
- [x] 🚫 get_tx_proof
- [x] 🚫 check_tx_proof
- [x] 🚫 get_spend_proof
- [x] 🚫 check_spend_proof
- [x] 🚫 get_reserve_proof
- [x] 🚫 check_reserve_proof
- [x] 🚫 get_transfers
- [x] 🚫 get_transfer_by_txid
- [x] 🚫 describe_transfer
- [x] ✅ sign
- [x] ✅ verify
- [x] ✅ export_outputs
- [x] import_outputs
- [x] ✅ export_key_images
- [x] import_key_images
- [x] ✅ make_uri
- [x] ✅ parse_uri
- [x] ✅ get_address_book
- [x] ✅ add_address_book
- [x] edit_address_book
- [x] delete_address_book
- [x] refresh
- [ ] auto_refresh
- [ ] rescan_spent
- [ ] start_mining
- [ ] stop_mining
- [ ] get_languages
- [ ] create_wallet
- [ ] generate_from_keys
- [ ] open_wallet
- [ ] restore_deterministic_wallet
- [ ] close_wallet
- [ ] change_wallet_password
- [ ] is_multisig
- [ ] prepare_multisig
- [ ] make_multisig
- [ ] export_multisig_info
- [ ] import_multisig_info
- [ ] finalize_multisig
- [ ] sign_multisig
- [ ] submit_multisig
- [x] ✅ get_version
