from flask import Flask
from db import mongo
from flask_pymongo import PyMongo , ObjectId
from eth_keys import keys
from cryptography.fernet import Fernet
import os
import json
import fileinput



file_path = 'keypairs.txt'  # Replace 'file.txt' with the actual file path

next_account = None

with open(file_path, 'r') as file:
    for line in file:
        pair = line.strip().split(',')
        next_account =  pair
        break




class Actor:


    def __init__(self):
        self.public_key = None
        self.private_key = None
        Actor.nbInstances +=  1
    
    def getPubKey(self):
        public_key_str = str(self.public_key)
        return  {'public key' : public_key_str}

    def signTranx(self):

        return

    def generate_key_pair():

                # Delete the first line of the file
        with fileinput.input(file_path, inplace=True) as file:
            first_line = True
            for line in file:
                if not first_line:
                    print(line, end='')
                first_line = False
        return { 'public_key' : str(next_account[1]) , 'private_key' : str(next_account[0])}


    
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