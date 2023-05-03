from web3 import Web3, WebsocketProvider
import json
import os


# create a web3 instance
web3 = Web3(WebsocketProvider('ws://127.0.0.1:8545'))
#Check Connection
t=web3.isConnected()
print(t)


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

# get the contract address from the blockchain by its name
contract_address = contracts['Farmer']['address']

# fetch the contract ABI from the blockchain
contract_abi = contracts['Farmer']['abi']

# create a contract object with the specified ABI and address
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
func_call = contract.functions['_isAdmin']().buildTransaction({
    "from": '0x2367C01119c7E5De8Db4a22c1f260f9a5c612C1b',
    "nonce": web3.eth.get_transaction_count('0x2367C01119c7E5De8Db4a22c1f260f9a5c612C1b'),
    "gasPrice": web3.eth.gas_price,
    "value": 0,
    "chainId": web3.eth.chain_id
})

signed_tx = web3.eth.account.sign_transaction(func_call, '0x84c0abb28e3357c112b30f513b6ae8b964bd9b676fcfee65e88d98b16943f911')

# get the status of the transaction
result = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
receipt = web3.eth.wait_for_transaction_receipt(result)
status = receipt['status']
print(status)

# get the return value of the function
logs = receipt['logs']
events = contract.events
return_value = event[0]['args']['returnValue']
print(events)

""" # get any exceptions generated
if status == 0:
    # get the reason for the failure
    revert_data = logs[-1]['data']
    exception = w3.eth.abi.decode_parameter('string', revert_data)
 """
""" result = contract.functions['_isAdmin']().call()
print(result) """


""" result = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
transaction_receipt = web3.eth.wait_for_transaction_receipt(result)
print(transaction_receipt) """



















""" # get the function object from the contract instance
function = getattr(contract.functions, '_isAdmin')


# build the transaction dictionary
txn_dict = {
    'from': '0x2367C01119c7E5De8Db4a22c1f260f9a5c612C1b',
    'to': contract_address,
    'data': function.encodeABI()
}

# sign the transaction with your private key and send it to the network
signed_txn = web3.eth.account.signTransaction(txn_dict, private_key='0x84c0abb28e3357c112b30f513b6ae8b964bd9b676fcfee65e88d98b16943f911')
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(tx_hash)  """

""" 
# define a route to send a specific transaction on the contract
@app.route('/', methods=['GET'])
def hello():
    return 'hello world'


@app.route('/send_transaction/<contract_name>/<function_name>', methods=['GET'])
def send_transaction(function_name, arguments):
    
    # get the contract address from the blockchain by its name
    contract_address = contracts[contract_name][address]

    # fetch the contract ABI from the blockchain
    contract_abi = contracts[contract_name][abi]

    # create a contract object with the specified ABI and address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    # convert the string of arguments to a list
    #arguments = json.loads(arguments)

    # get the function object from the contract instance
    function = getattr(contract.functions, function_name)


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





 """