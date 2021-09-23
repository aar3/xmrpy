import os
from flask import Flask, response
from xmrpy import Wallet

app = Flask(__name__)
wallet = Wallet()


@app.route("/", methods=["GET"])
def home():
    return "monero proxy app"


@app.route("/transfer", methods=["POST"])
async def transfer(request):
    destinations = request.data["destinations"]
    account_index = request.data["account_index"]
    subaddress_indices = request.data["subaddress_indices"]

    r = await wallet.transfer_sign_submit(destinations, account_index, subaddress_indices)

    return response(data={"tx_hash_list": r.result.tx_hash_list})


@app.route("/balance", methods=["GET"])
async def get_galance(request):
    account_index = request.data["account_index"]
    address_indices = request.data["address_indices"]
    r = await wallet.get_balance(account_index, address_indices)

    return response(data={"balance": r.result.balance, "unlocked_balance": r.result.unlocked_balance})


if __name__ == "__main__":

    app.run(host=os.environ["HOST"], port=os.environ["PORT"])
