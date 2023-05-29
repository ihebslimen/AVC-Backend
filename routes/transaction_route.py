from flask import Flask, jsonify, request
from eth_abi.exceptions import DecodingError
from web3 import Web3, WebsocketProvider
from models.transaction import Transaction
import json
import os
import logging
from blueprints.user import user_bp
from web3 import Web3
import binascii


# create a web3 instance
ENDPOINT = 'ws://127.0.0.1:8545'
web3 = Web3(WebsocketProvider(ENDPOINT))
#Check Connection
#t=web3.isConnected()

contracts =  {}
# Set the path to the folder containing the files
folder_path = '../AVC-Blockchain/build/contracts'

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a regular file (not a folder or symlink)
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename), 'r', encoding="utf-8") as f: # adding utf-8 encoding for windows users
            contract = f.read()
            contract_json = json.loads(contract)
            contracts[contract_json['contractName']] = {}
            contracts[contract_json['contractName']]['abi'] = contract_json['abi']
            if '1337' in contract_json['networks'] and 'address' in contract_json['networks']['1337']:
                contracts[contract_json['contractName']]['address'] = contract_json['networks']['1337']['address']




@user_bp.route('/send_transaction', methods=['POST'])
def send_transaction():
    data = request.get_json()
    public_key = data['public_key']
    private_key = data['private_key']
    contract_abi= {}
    # get the contract address from the blockchain by its name
    contract_address = contracts[data['contract_name']]['address']
    # fetch the contract ABI from the blockchain
    contract_abi = contracts[data['contract_name']]['abi']
    # create a contract object with the specified ABI and address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    estimated_gas = contract.functions[data['function_name']]().estimate_gas({"from": public_key,"value": 0})
    gasLimit= estimated_gas * 1.2

    transaction = Transaction.createTx(
        web3.eth.get_transaction_count(public_key),
        public_key, 
        web3.eth.gas_price, 
        gasLimit, 
        web3.eth.chain_id,
        0
        )

    if len(data['arguments']) == 0 :
        functionBuild = contract.functions[data['function_name']]().buildTransaction(transaction)
    else:
        functionBuild = contract.functions[data['function_name']](*data['arguments']).buildTransaction(transaction)

    signed_tx = web3.eth.account.sign_transaction(functionBuild, private_key)

    # code to send transaction
    signed_tx = web3.eth.account.sign_transaction(functionBuild, private_key)
    try:
        # get the status of the transaction
        result = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(result)
        status = receipt['status']
        if status == 1 :
            res = jsonify({'Message': 'Transaction succeeded'})
            res.status_code = 200
        else:
            res = jsonify({'Error': 'Transaction failed'})
            res.status_code = 404
        return res

    except Exception as e:
        return(f"Unexpected error: {str(e)}")




@user_bp.route('/transaction_history',  methods=['GET'])
def get_transactions():
    transactions = []
    abi= {}
    # Get the latest block number
    block_number = web3.eth.block_number

    # Retrieve transactions for each block
    for i in range(block_number + 1):
        block = web3.eth.get_block(i, full_transactions=True)
        transactions.extend(block.transactions)
    logs_dict = []
    for log in transactions:
        
        if log.to == contracts['Farmer']['address']:
            """ print(log.to)
            print(log.hash) """
            receipt = web3.eth.wait_for_transaction_receipt(log.hash)
            print(receipt)
        """ log_dict = {}
        for key, value in log.items():
            
            if isinstance(value, bytes):
                log_dict[key] = binascii.hexlify(value).decode('utf-8')
            else:
                log_dict[key] = value
        logs_dict.append(log_dict)

    # Serialize the list of dictionaries to JSON
    serialized_logs = json.dumps(logs_dict)
    #print(serialized_logs)
    for log in logs_dict:
        print(log)
        if contracts['Farmer']['address'] == log['to']:
            print(log['to'])
 """

    return 'hello'




""" def get_transaction_history():

    event_filter = {
        'fromBlock': 0,  # Starting block number
        'toBlock': 'latest',  # Ending block number (or 'latest' for the latest block)
    }

    

    sync_status = web3.eth.syncing


    # Retrieve the event logs
    logs = web3.eth.get_logs(event_filter)
    # Iterate over logs
    for log in logs:
        # Get transaction details
        tx_hash = log.transactionHash
        transaction = web3.eth.getTransaction(tx_hash)
        if transaction.get('contractAddress'):
            contract_address = transaction['contractAddress']
            print(f"Contract Address: {contract_address}")
        else:
            print("The transaction is not a contract creation transaction.")

        # Print transaction details
        print("Transaction Hash:", transaction['hash'].hex())
        print("Block Number:", transaction['blockNumber'])
        print("From:", transaction['from'])
        print("To:", transaction['to'])
        print("Value:", transaction['value'])
        print("Gas Price:", transaction['gasPrice'])
        print("Gas Limit:", transaction['gas'])
        #print("Input Data:", transaction['input'])
        print("-------------------------------")
        print("-------------------------------")


        return("hello")

 """

"""    # Convert logs to dictionaries
    serialized_logs = []
    for log in logs:
        serialized_log = dict(log)
        serialized_logs.append(serialized_log)

    # Serialize the list of logs
    serialized_logs_str = json.dumps(serialized_logs, cls=HexBytesEncoder)
    print(serialized_logs_str)

    return(serialized_logs_str)
 """



@user_bp.route('/send_transaction1', methods=['POST'])
def send_transaction1():
    data = request.get_json()
    public_key = data['public_key']
    private_key = data['private_key']
    contract_abi= {}
    # get the contract address from the blockchain by its name
    contract_address = contracts[data['contract_name']]['address']
    # fetch the contract ABI from the blockchain
    contract_abi = contracts[data['contract_name']]['abi']
    # create a contract object with the specified ABI and address

  
   
    # Set the function name and encoded data
    function_name = data['function_name']
    for  func  in contract_abi:
        if 'name' in func:
            if func['name'] == function_name:
                function_abi = func
                print(func, '\n \n')
                break
            


    # Encode the function selector
    function_selector = Web3.keccak(text=f"{function_name}()")[:4].hex()

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    encoded_function_call = contract.encodeABI(function_name)
    # Encode the function arguments
    #encoded_inputs = encode_abi([input['type'] for input in function_abi['inputs']], function_inputs).hex()

    # Combine the function selector and arguments
    #encoded_data = f"0x{function_selector}{encoded_inputs}"

    # Set the transaction parameters
    transaction_params = {
        'to': contract_address,
        'data': encoded_function_call,
        'gas': web3.eth.estimate_gas({'to': contract_address, 'data': encoded_function_call}),
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(public_key),
    }

    # Sign the transaction
    signed_transaction = web3.eth.account.sign_transaction(transaction_params, private_key)

    # Send the signed transaction to the network
    transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)

    # Wait for the transaction to be mined
    transaction_receipt = web3.eth.wait_for_transaction_receipt(transaction_hash)

    # Print the transaction receipt
    print(transaction_receipt)
    return jsonify( transaction_receipt['status'])

