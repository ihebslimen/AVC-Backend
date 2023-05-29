from web3 import Web3, WebsocketProvider
import json
import os
from dotenv import load_dotenv

load_dotenv()


# create a web3 instance
ENDPOINT = os.environ.get('ENDPOINT')
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

