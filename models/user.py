from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from db import mongo
from models.actor import Actor


class User(Actor):
    def __init__(self,_id, cin, name, email, phone, role, type,state, actor_id):
        self._id
        self.cin = cin
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.type = type
        self.state= state
        self.actor_id = actor_id

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        result = []
        for user in users:
            result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'],'public_key' : user['public_key']})
        return result

    @staticmethod
    def get_one_user(_id):
        user = mongo.db.users.find_one({'_id': ObjectId(_id)})
        return {'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'], 'public_key' : user['public_key']}

    @staticmethod
    def filter_users(query):
        users = mongo.db.users.find(query)
        result = []
        for user in users:
            result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'], 'public_key' : user['public_key']})
        return result
    @staticmethod
    def create_user(cin, name, email, phone, role, type ='', actorInfoJson = ''):
        keys = Actor.generate_key_pair()
        if role == 'admin':
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role,"public_key": keys['public_key'],"private_key" : keys['private_key']}
            res = mongo.db.users.insert_one(user)
        elif role == 'user':
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role, 'type' : type,"public_key": keys['public_key'],"private_key" : keys['private_key'] }
            user_id = mongo.db.users.insert_one(user).inserted_id
            actorInfoJson['user_ref'] = user_id
            print('##############',actorInfoJson)
            res = mongo.db[type].insert_one(actorInfoJson)
        print(res.acknowledged)
        return res.acknowledged


    @staticmethod
    def update_user(_id , query):
        res = mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': query})
        return res.acknowledged
    
    @staticmethod
    def delete_user(_id):
        res = mongo.db.users.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
