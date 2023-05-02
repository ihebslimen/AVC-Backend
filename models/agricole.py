from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId



class Agricole(Actor):
    def __init__(self,_id, type,localisation):
        super.__init__(_id,  type)
        self.localisation = localisation


    @staticmethod
    def get_all_agricoles():
        agricoles = mongo.db.agricole.find()
        result = []
        for agricole in agricoles:
            result.append({'_id': str(agricole['_id']), 'localisation' : agricole['localisation']})
        return result

    @staticmethod
    def get_one_agricole(_id):
        agricole = mongo.db.agricole.find_one({'_id': object(_id) })
        return {'_id': str(agricole['_id']), 'localisation' : agricole['localisation']}

    @staticmethod
    def create_agricole( localisation):
        agricole = {'localisation' : localisation}
        mongo.db.agricole.insert_one(agricole)

    @staticmethod
    def update_agricole(_id, localisation):
        mongo.db.agricole.update_one({'_id': ObjectId(_id)}, {'$set': {'localisation' : localisation}})

    @staticmethod
    def delete_agricole(_id):
        mongo.db.agricole.delete_one({'_id':ObjectId(_id)})
