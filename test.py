from flask import Flask, jsonify
from web3 import Web3, HTTPProvider
import json

app = Flask(__name__)

# create a web3 instance
web3 = Web3(HTTPProvider('127.0.0.1:8545'))

# define a route to send a specific transaction on the contract
@app.route('/send_transaction/<contract_name>/<function_name>/<arguments>', methods=['GET'])
def send_transaction(function_name, arguments):
    
    # get the contract address from the blockchain by its name
    contract_address = web3.eth.contract().address

    # fetch the contract ABI from the blockchain
    contract_abi = web3.eth.contract(address=contract_address).abi

    # create a contract object with the specified ABI and address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    # convert the string of arguments to a list
    arguments = json.loads(arguments)

    # get the function object from the contract instance
    function = getattr(contract.functions, function_name)(*arguments)

    # get the gas estimate for the transaction
    gas_estimate = function.estimateGas()

    # build the transaction dictionary
    txn_dict = {
        'from': '0x5E6907F11C85a69e7B4c85547ce79A41A762a79F',
        'to': contract_address,
        'data': function.encodeABI()
    }

    # sign the transaction with your private key and send it to the network
    signed_txn = web3.eth.account.signTransaction(txn_dict, private_key='0x2eba5d8a02ed0db3edc8a971b9c9ecee496aae375601b231f16cb2e7c2399099')
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return jsonify({'transaction_hash': web3.toHex(tx_hash)})


if __name__ == '__main__':
    app.run(debug=True)
