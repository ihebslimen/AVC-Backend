from web3models.Farmer import Farmer
from config_web3 import web3
from config_web3 import contracts

f = Farmer(
    web3,
    {
        "pub_key" : "0x4747DC6f644A9d5Bc4Ae48BE2cC3179735AeC94F",
        "priv_key" : "0x70b78d8f8a95adf1e7a7d223cfeb3709ff828672839261614b07af9c51eec7a6"
    },
    "0x2809325E9e1695887cfD9F63Ad93bB26E8064e2D",
    0x645e7a488b96b66d55bde08e,
    "14415698",
    34567890,
    "farmer"
)

print(f)
f.save()
""" 
from web3 import Web3, WebsocketProvider,HTTPProvider
import os
import json

# Connect to a local Ethereum node (e.g. Ganache)
web3 = Web3(WebsocketProvider('ws://127.0.0.1:8545'))




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
            


contract = web3.eth.contract(address=contracts['Farmer']['address'], abi=contracts['Farmer']['abi'])

#print(web3.eth.get_transaction("0x78a8dbf67b6b5daf7a1da1b272639a350a56e69f5fb0509c21024352ee1b69be"))
#print(contracts['Farmer'])

#print(contracts)

# Call a function on the contract
#result = contract.functions.addNewAdmin("0x9AAE48370359b03f9505f6723095A736b44b9c27").transact({"from" : accounts[0]})
#event_filter = contract.events.AdminAdded.create_filter(fromBlock='latest')
#event_filter = contract.events.AdminAdded.create_filter(fromBlock = "0x0", toBlock = "latest")
#print(result)
events = contract.events.FarmerCreated.get_logs(fromBlock=contracts['Farmer']['blockNumber'])
#print(events)

print(contracts['Farmer']['address'])
event_filter = web3.eth.filter({"fromBlock": "earliest",
    "toBlock": "latest", "address": contracts['Farmer']['address']})

    


print(event_filter.get_all_entries())

event_filter = web3.eth.filter({"fromBlock": "earliest",
    "toBlock": "latest", "address": "0x4747DC6f644A9d5Bc4Ae48BE2cC3179735AeC94F"})
print("\n\n\n\n", )

print(web3.eth.get_transaction_receipt("0x12b05f6717b17deaba718516de9bd7a7303c31ba1631400e000f2986eba9678e")) """