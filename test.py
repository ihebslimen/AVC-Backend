from web3 import Web3, WebsocketProvider,HTTPProvider
import os
import json

# Connect to a local Ethereum node (e.g. Ganache)
web3 = Web3(HTTPProvider('http://127.0.0.1:8545'))




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


# Create a contract instance
contract = web3.eth.contract(address=contracts['Farmer']['address'], abi=contracts['Farmer']['abi'])

# Call a function on the contract
result = contract.functions._isAdmin().call({'from': web3.eth.accounts[0]})
# Print the result
print(result)