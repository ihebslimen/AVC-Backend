from web3 import Web3, WebsocketProvider
import json
import os
from blueprints.shared import shared_bp


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





# define a route to send a specific transaction on the contract
@app.route('/send_transaction/<contract_name>/<function_name>', methods=['GET'])
def send_transaction(function_name, arguments):
    
    # get the contract address from the blockchain by its name
    contract_address = contracts[contract_name]['address']

    # fetch the contract ABI from the blockchain
    contract_abi = contracts[contract_name]['abi']

    # create a contract object with the specified ABI and address
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    # get the public key of the user 
    
    func_call = contract.functions[function_name]().buildTransaction({
        "from": '0x875f357e3b585a4Ae4B469491F3980C8818C7268',
        "nonce": web3.eth.get_transaction_count('0x875f357e3b585a4Ae4B469491F3980C8818C7268'),
        "gasPrice": web3.eth.gas_price,
        "value": 0,
        "chainId": web3.eth.chain_id
    })

    signed_tx = web3.eth.account.sign_transaction(func_call, '0xd3add8792fcfb41f0f8cb767aaafdaafae2ab6403d917ac690c0fdab63752171')

    # get the status of the transaction
    result = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(result)
    status = receipt['status']
    print(status)
    if status == 1:
        try:
            tx = web3.eth.get_transaction(result)
        except Exception as e:
            print("Error getting transaction:",e)
        replay_tx = {
            'to': tx['to'],
            'from': tx['from'],
            'value': tx['value'],
            'data': tx['input'],
            'gas': tx['gas'],
        }
        # replay the transaction locally:
        try:
            ret = web3.eth.call(replay_tx, tx.blockNumber - 1)
            print('Transaction succeed , return value :', ret)
        except Exception as e: 
            print('Transaction succeed, no return value',str(e))
    else:
        print('Transaction failed')


    return jsonify({'transaction_hash': web3.toHex(tx_hash)})




