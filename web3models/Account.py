from web3 import Web3, WebsocketProvider
from flask import Flask, jsonify, request

from config_web3 import web3
from config_web3 import contracts
import os

class Account:
    def __init__(self, pub_key , priv_key) -> None:
        self.pub_key = pub_key
        self.priv_key = priv_key
        self.contract_address = contracts["Farmer"]["address"]
        self.contract_abi = contracts["Farmer"]["abi"]
        self.FarmerContract =web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
        

    def addFarmer(self, _address, _id, _name, _phone, _info = "data", _data = "") -> None:

 
        functionCall = self.FarmerContract.functions.addFarmer(
            _address, _id, _name, _phone, _info, _data
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction failed")
    def addNewAdmin(self,_address):

 
        functionCall = self.FarmerContract.functions.addNewAdmin(
            _address
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction successful")

    def removeAdmin(self,_address):

 
        functionCall = self.FarmerContract.functions.removeAdmin(
            _address
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction successful")

    def addProduct(self,_farmeraddr,_farmId,_date,_TreeId):
        functionCall = self.FarmerContract.functions.addAgroCulturePlantBased(
            _farmeraddr,_farmId,_date,_TreeId
        
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction successful")

    def addFarm(self,_farmeraddr, _farmName, _lat, _lon,_crops, _seeds,_uri):

        functionCall = self.FarmerContract.functions.addFarm(
            _farmeraddr, _farmName, _lat, _lon,_crops, _seeds,_uri
        
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction failed")

    def addTree(self,_farmeraddr, uri,_Age,_Crop, _Seed,_FarmID):
        functionCall = self.FarmerContract.functions.addTree(
            _farmeraddr, uri,_Age,_Crop, _Seed,_FarmID
        
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
        if tx_receipt['status'] == 1:

            return("transaction successful")
        else:
            return("transaction failed")


    
