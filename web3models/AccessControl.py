from web3 import Web3, WebsocketProvider
from flask import Flask, jsonify, request

from config_web3 import web3
from config_web3 import contracts
import os


contract_address = contracts["AccessControl"]["address"]
contract_abi = contracts["AccessControl"]["abi"]
AccessControlContract =web3.eth.contract(address=contract_address, abi=contract_abi)


class AccessControl:
    def __init__(self, pub_key , priv_key) -> None:
        self.pub_key = pub_key
        self.priv_key = priv_key
        #self.contract_address = contracts["AccessControl"]["address"]
        #self.contract_abi = contracts["AccessControl"]["abi"]
        #AccessControl =web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        

    def hasUserType(self, _addr,type_ref) -> None:
        functionCall = AccessControlContract.functions.hasUserType(
             _addr, type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")


    def setUserType(self, _addr,_type_ref) -> None:
        functionCall = AccessControlContract.functions.setUserType(
             _addr,_type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")
        

    def delUserType(self, _addr,_type_ref) -> None:
        functionCall = AccessControlContract.functions.delUserType(
             _addr,_type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def delUserType(self, _addr,_type_ref) -> None:
        functionCall = AccessControlContract.functions.delUserType(
             _addr,_type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")