from flask import Flask
from db import mongo
from flask_pymongo import PyMongo , ObjectId
from eth_keys import keys
from cryptography.fernet import Fernet
import os
import json

class Actor:
    nbInstances = 0

    def __init__(self):
        self.public_key = None
        Actor.nbInstances +=  1
        self.generate_key_pair()
    
    def getPubKey(self):
        public_key_str = str(self.public_key)
        return  {'public key' : public_key_str}

    def signTranx(self):

        return

    def generate_key_pair(self):
        # Generate a new private key
        private_key = keys.PrivateKey(os.urandom(32)) 
        # Derive the public key from the private key
        public_key = private_key.public_key
        # Encrypt the private key and save it securely to a file
        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(private_key.to_bytes())
        with open('private_key.txt', 'wb') as f:
            f.write(cipher_text)
        # Erase any trace of the private key from the program
        del private_key
        self.public_key = public_key

    def negociate(self):
        return
    def sendTransaction(self):
        return
    def receiveTransaction(self):
        return
    def updateProductState(self):
        return
    def enableContest(self):
        return
    def genLeaderboard(self):
        return
    def verifyReceivingConditions(self):
        return
    def updateDeliveries(self):
        return
    def alertViolation(self):
        return
    def getData(self):
        return