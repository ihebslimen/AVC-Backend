from web3 import Web3, WebsocketProvider
from config_web3 import web3
from config_web3 import contracts
import os


class Admin:
    def __init__(self, _web3, _keys, _address) -> None:
        self.web3 = _web3
        self.address = _address
        self.keys = _keys # admin keys
        self.contract_address = contracts["Farmer"]["address"]
        self.contract_abi = contracts["Farmer"]["abi"]
        self.FarmerContract =self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        

    def save(self):
        print(self.web3.eth.accounts)
        functionCall = self.contract.functions.addFarmer(
            self.address, self.id, self.name, self.phone, self.info, self.data
        ).build_transaction(
            {   
                'from' : self.keys["pub_key"],
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count('0x5b70559bcccece4c410e4d7016095f3694097bf2fd2bd22d5f4d3e5371951bd5'),
                "chainId" : self.web3.eth.chain_id
            }
        )
        
        signed_tx = self.web3.eth.account.sign_transaction(functionCall, private_key=self.keys["priv_key"])
        send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)

        print(tx_receipt)
    

    



