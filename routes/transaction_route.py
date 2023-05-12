from flask import Flask, jsonify, request
from eth_abi import decode_abi
from eth_abi.exceptions import DecodingError
from web3 import Web3, WebsocketProvider
from models.transaction import Transaction
import json
import os
import logging
from blueprints.user import user_bp


# create a web3 instance
ENDPOINT = os.environ.get('ENDPOINT')
web3 = Web3(WebsocketProvider(ENDPOINT))
#Check Connection
t=web3.isConnected()

contracts =  {}
# Set the path to the folder containing the files
folder_path = '../AVC-Blockchain-master/build/contracts'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a regular file (not a folder or symlink)
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename), 'r') as f:
            contract = f.read()
            contract_json = json.loads(contract)
            contracts[contract_json['contractName']] = {}
            contracts[contract_json['contractName']]['abi'] = contract_json['abi']
            if '1337' in contract_json['networks'] and 'address' in contract_json['networks']['1337']:
                contracts[contract_json['contractName']]['address'] = contract_json['networks']['1337']['address']


@user_bp.route('/', methods=['GET'])
def hello():
    return 'hello user from tx'


@user_bp.route('/send_transaction', methods=['POST'])
def send_transaction():

    data = request.get_json()
    contract_abi= {}
    # get the contract address from the blockchain by its name
    contract_address = contracts[data['contract_name']]['address']
    # fetch the contract ABI from the blockchain
    contract_abi = contracts[data['contract_name']]['abi']
    # create a contract object with the specified ABI and address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    estimated_gas = web3.eth.estimate_gas({"from": data['sender'],'to': contract_address,"value": 0})
    gasLimit= estimated_gas * 1.2

    transaction = Transaction.createTx(
        web3.eth.get_transaction_count(data['sender']),
        data['sender'], 
        web3.eth.gas_price, 
        gasLimit, 
        web3.eth.chain_id,
        0
        )

    if len(data['arguments']) == 0 :
        functionBuild = contract.functions[data['function_name']]().buildTransaction(transaction)
    else:
        functionBuild = contract.functions[data['function_name']](*data['arguments']).buildTransaction(transaction)

    signed_tx = web3.eth.account.sign_transaction(functionBuild, data['private_key'])

    # code to send transaction
    signed_tx = web3.eth.account.sign_transaction(functionBuild, data['private_key'])
    try:
        # get the status of the transaction
        result = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(result)
        status = receipt['status']
        if status == 1 :
            response = jsonify({'message': 'Transaction succeeded'})
            response.status_code = 200
            
        else:
            response = jsonify({'message': 'Transaction failed'})
            response.status_code = 400

        return response

    except Exception as e:
        return(f"Unexpected error: {str(e)}")

