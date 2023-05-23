from web3models.Farmer import Farmer
from web3models.Account import Account , contracts,web3


A = Account( "0x7DCE5a8F76ddA78904cB5a7F6dbC9d7c509B0A11",  "0x90ad4aa23e61a226fb11ff6fe7b0c30b03a98ec2b87c26038c2525f609be55e1")
F = Account('0x251BeeDBF1D9E95A72AA7a3b73a14190d5300904', "0x4057963739a3f34e6c14a70afbb1d907320e541245dae69a0860ca830c0040de")

#result = A.addFarmer('0x251BeeDBF1D9E95A72AA7a3b73a14190d5300904', 5, 'iheb1', 6)
event_filter = web3.eth.filter({"fromBlock": "earliest",
    "toBlock": "latest", "address": contracts['Farmer']['address']})

    


print(event_filter.get_all_entries())

for log in event_filter.get_all_entries():
    # Access the relevant information from the log
    decoded_data = A.FarmerContract.decode_function_input(log['data'])    # Extract the desired data from the event_data
    print(decoded_data)
    # Modify the code below to match the structure of your event and the information you want to extract
""" 
    # Example: Extracting the farmer's address and the farm ID
    farmer_address = event_data.args.farmerAddress
    farm_id = event_data.args.farmId

    # Print the extracted information
    print("Farmer Address:", farmer_address)
    print("Farm ID:", farm_id)
 """
""" 
contract = web3.eth.contract(address=contracts['Farmer']['address'], abi=contracts['Farmer']['abi'])

A = Account( "0xD3372029C99865A788a7501a681570B54416B143",  "0xeb29acf3af18b6586ecf56bb9d446869f58c8ae0e038f6f592eb91d1b447a35f")
F = Account('0x2e101380207c1720217d3831f3c44E42ae805BBb', "0x00a98836bd6ae1ab9c9f297608f7e296fa6b5e777bb10ea48e749060d0b944ff")
#result = A.addFarmer('0x2e101380207c1720217d3831f3c44E42ae805BBb', 3, 'iheb', 5)
# Get the event object
event = contract.events.addFarm

# Get the event logs
event_logs = event.getLogs(fromBlock=w3.eth.block_number - 1000, toBlock='latest')

# Process the event logs
for log in event_logs:
    # Access the relevant information from the log
    event_data = event().processLog(log)
    # Extract the desired data from the event_data
    # Modify the code below to match the structure of your event and the information you want to extract

    # Example: Extracting the farmer's address and the farm ID
    farmer_address = event_data.args.farmerAddress
    farm_id = event_data.args.farmId

    # Print the extracted information
    print("Farmer Address:", farmer_address)
    print("Farm ID:", farm_id) """
""" 
events = contract.events.addFarmer.get_logs(fromBlock=contracts['Farmer']['blockNumber'])

print(events) """
""" 
result1  = A.addFarm('0x545fcF8E20Fe0380903b66B653b898FB8C7Ad19A', 'iheb farm 3', '', '', ['Corp'],['Seed'],'')

print(result)
# Define the event ABI
event_abi = contract.events.addFarm._get_event_abi()

# Iterate through the logs
for log in events:
    # Decode the log using the event ABI
    decoded_log = w3.eth.abi.decode_log(event_abi, log.data, log.topics)

    # Extract relevant information from the decoded log
    # Modify the code below to match the structure of your event and the information you want to extract

    # Example: Extracting the farmer's address and the farm ID
    farmer_address = decoded_log['args']['farmerAddress']
    farm_id = decoded_log['args']['farmId']

    # Print the extracted information
    print("Farmer Address:", farmer_address)
    print("Farm ID:", farm_id)




 """

#result2 = A.addTree('0x54cCED390420d383b5602334F615ecb26eC6e4C2', '',1,'Crop', 'Seed',3)
    

#result3 = F.addProduct('0x2D84Ce11482f380F4492Dd254b4aD2D49FC2F35A',1,'today',2)

#print(result2)










#print(result)

""" result = A.addFarmer(
            "0x2D84Ce11482f380F4492Dd254b4aD2D49FC2F35A",
            0x645e7a488b96b66d55bde08e,
            "iheb",
            61848468,
            "farmer"
        ) """
""" f = Farmer(
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
) """

""" print(f)
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

print(web3.eth.get_transaction_receipt("0x12b05f6717b17deaba718516de9bd7a7303c31ba1631400e000f2986eba9678e"))