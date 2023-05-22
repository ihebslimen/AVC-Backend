from web3 import Web3, WebsocketProvider,HTTPProvider
import os
import json

# Connect to a local Ethereum node (e.g. Ganache)
web3 = Web3(WebsocketProvider('ws://127.0.0.1:8545'))




contracts =  {}
# Set the path to the folder containing the files
folder_path = '../AVC-Blockchain/build/contracts'
accounts = web3.eth.accounts
#print(accounts)

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a regular file (not a folder or symlink)
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename), 'r', encoding="utf-8") as f:
            contract = f.read()
            contract_json = json.loads(contract)
            contracts[contract_json['contractName']] = {}
            contracts[contract_json['contractName']]['abi'] = contract_json['abi']
            
            #print(contract_json['networks'])
            if '1337' in contract_json['networks'] and 'address' in contract_json['networks']['1337']:
                contracts[contract_json['contractName']]['address'] = contract_json['networks']['1337']['address']
                tx_hash = contract_json['networks']['1337']["transactionHash"]
                contracts[contract_json['contractName']]['transactionHash'] = tx_hash
                contracts[contract_json['contractName']]['blockNumber'] = web3.eth.get_transaction(tx_hash ).get("blockNumber")
            



# Create a contract instance
contract = web3.eth.contract(address=contracts['Farmer']['address'], abi=contracts['Farmer']['abi'])

#print(web3.eth.get_transaction("0x78a8dbf67b6b5daf7a1da1b272639a350a56e69f5fb0509c21024352ee1b69be"))
#print(contracts['Farmer'])

#print(contracts)

# Call a function on the contract
#result = contract.functions.addNewAdmin("0x6BA331FA95d9646EC92aadA49bEf483961bf01d6").transact({"from" : accounts[0]})
#event_filter = contract.events.AdminAdded.create_filter(fromBlock='latest')
#event_filter = contract.events.AdminAdded.create_filter(fromBlock = "0x0", toBlock = "latest")
#print(result)
events = contract.events.AdminAdded.get_logs(fromBlock=contracts['Farmer']['blockNumber'])
print(events)
#print(contract.functions.getAllAdmins().call())


data = {
    "public_key" : "0x14cF2d8cd6c0fB1C86B8845fd2a100C0804eebc7",
    "private_key" : "0xe6a1a55d483b18a9aeb785dbb73311d38ea35d0894d6fb982d070761d10c3fc2",
    "contract_name" : "Farmer",
    "function_name" : "getAllAdmins"

}
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