from flask import Flask
from flask_pymongo import PyMongo
from db import mongo
from flask_pymongo import PyMongo , ObjectId



class Actor:
    nbInstances = 0

    def __init__(self,_id, privateKey, publicKey, type):
        self._id
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.type = type
        Actor.nbInstances +=  1

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