from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId



class Violation():
    def __init__(self,msg, userRef):
        super.__init__(_id,  type)
        self.msg = msg
        self.userRef = userRef


    @staticmethod
    def get_all_violations():
        violations = mongo.db.violation.find()
        result = []
        for violation in violations:
            result.append({'_id': str(violation['_id']), 'msg': violation['msg'], 'userRef' : violation['userRef']})
        return result
        
    @staticmethod
    def filter_violations(query):
        if '_id' in query:
            query['_id'] = ObjectId(query[value])
        violations = mongo.db.violation.find(query)
        result = []
        for violation in violations:
            result.append({'_id': str(violation['_id']), 'msg': violations['msg'], 'userRef' : violations['userRef']})
        return result

    
    @staticmethod
    def get_one_violation(_id):
        violation = mongo.db.violation.find_one({'_id':ObjectId(_id)})
        return {'_id': str(violation['_id']), 'msg': violation['msg'], 'userRef' : violation['userRef']}

    @staticmethod
    def create_violation( msg, userRef):
        violation = {'msg': msg , 'userRef':userRef}
        res = mongo.db.violation.insert_one(violation)
        return res.acknowledged

 
    @staticmethod
    def delete_violation(_id):
        res = mongo.db.violation.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
