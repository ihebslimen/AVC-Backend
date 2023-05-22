from web3 import Web3, WebsocketProvider
from config_web3 import contracts
import os


class Farmer:
    def __init__(self, _web3, _keys, _address, _id, _name, _phone, _info = "data", _data = "") -> None:
        self.web3 = _web3
        self.address = _address
        self.id = _id
        self.name = _name
        self.phone = _phone
        self.info = _info
        self.data = _data
        self.keys = _keys # admin keys
        self.contract_address = contracts["Farmer"]["address"]
        self.contract_abi = contracts["Farmer"]["abi"]
        self.contract =self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        

    def save(self):
        print(self.web3.eth.accounts)
        functionCall = self.contract.functions.addFarmer(
            self.address, self.id, self.name, self.phone, self.info, self.data
        ).build_transaction(
            {   
                'from' : self.keys["pub_key"],
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(self.keys["pub_key"]),
                "chainId" : self.web3.eth.chain_id
            }
        )
        
        signed_tx = self.web3.eth.account.sign_transaction(functionCall, private_key=self.keys["priv_key"])
        send_tx = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = self.web3.eth.wait_for_transaction_receipt(send_tx)

        print(tx_receipt)
    

    



