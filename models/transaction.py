from flask import Flask
from db import mongo
from flask_pymongo import PyMongo , ObjectId
from eth_keys import keys
from cryptography.fernet import Fernet
import os
import json

class Transaction:
    def __init__(self,nonce, gasPrice, gasLimit, chainId, data, toAddress, fromAddress,value):
        self.nonce = nonce
        self.gasPrice = gasPrice
        self.gasLimit = gasLimit
        self.chainId = chainId
        self.toAddress = toAddress
        self.fromAddress = fromAddress
        self.data = data
        self.value= value

    def createTx( nonce, fromAddress, gasPrice,gasLimit, chain_id, value):

        tx= {
        "nonce": nonce,
        "from": fromAddress,
        "value": value,
        "chainId": int(chain_id),
        "gas": int(gasLimit),
        "gasPrice": int(gasPrice)
        }

        

        return tx

    def signTx(self,tx):
        signedTx = tx
        return signedTx




    