from flask import Flask
from db import mongo
from flask_pymongo import PyMongo , ObjectId
from eth_keys import keys
from cryptography.fernet import Fernet
import os
import json

class Transaction:
    def __init__(self, chainId, data, accountAddr, contractAddr, abi):
        self.chainId = chainId
        self.data = data
        self.accountAdd = accountAddr
        self.contractAddr = contractAddr
        self.abi = abi

    def createTx(self, function_name, function_args):

        contract = w3.eth.contract(address=self.contractAddr, abi=self.abi)

        # get the function object from the contract instance
        function = contract.functions[function_name](*function_args)

        # encode the function call data
        tx_data = function.encodeABI()
        
        tx=  {
            "chainId": self.chainId,
            "data": tx_data,
            "from": self.accountAdd,
            "to": self.contractAddr
        }




    def signTx(self,tx):
        signedTx = tx
        return signedTx




    