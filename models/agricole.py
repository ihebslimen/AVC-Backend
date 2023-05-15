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
            result.append({'_id': str(agricole['_id']), 'localisation' : agricole['localisation'], 'user_ref' : agricole['user_ref']})
        return result

    @staticmethod
    def get_one_agricole(_id):
        agricole = mongo.db.agricole.find_one({'_id': ObjectId(_id) })
        return {'_id': str(agricole['_id']), 'localisation' : agricole['localisation'], 'user_ref' : agricole['user_ref']}

    @staticmethod
    def filter_agricole(query):
        if '_id' in query:
            query['_id'] = ObjectId(query[value])
        agricoles = mongo.db.agricole.find(query)
        result = []
        for agricole in agricoles:
            result.append({'_id': str(agricole['_id']), 'localisation' : agricole['localisation'], 'user_ref' : agricole['user_ref']})
        return result
        
    @staticmethod
    def create_agricole( localisation):
        agricole = {'localisation' : localisation}
        res = mongo.db.agricole.insert_one(agricole)
        return res.acknowledged

    @staticmethod
    def update_agricole(_id, query):
        res = mongo.db.agricole.update_one({'_id': ObjectId(_id)}, {'$set': query})
        return res.acknowledged

    @staticmethod
    def delete_agricole(_id):
        res = mongo.db.agricole.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
