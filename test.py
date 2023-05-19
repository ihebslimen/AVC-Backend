from web3 import Web3, WebsocketProvider,HTTPProvider
import os
import json

# Connect to a local Ethereum node (e.g. Ganache)
web3 = Web3(WebsocketProvider('ws://192.168.1.216:8545'))




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