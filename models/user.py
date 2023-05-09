from flask import Flask
from flask_pymongo import PyMongo, ObjectId
from db import mongo


class User():
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
            result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user[type]})
        return result

    @staticmethod
    def get_one_user(_id):
        user = mongo.db.users.find_one({'_id': ObjectId(_id)})
        return {'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user[type]}

    @staticmethod
    def filter_users(key, value):
        users = mongo.db.users.find({key:value})
        result = []
        for user in users:
            result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user[type]})
        return result
    @staticmethod
    def create_user(cin, name, email, phone, role, type, actorInfoJson):
        if role == 'admin':
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role, 'type' : None}
        elif role == 'user':
            actor_id = mongo.db[type].insert_one(actorInfoJson).inserted_id
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role, 'type' : type, 'actor_id': ObjectId(actor_id) }
        mongo.db.users.insert_one(user)


    @staticmethod
    def update_user(_id , cin, name, email, phone, role, type):
        mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role, 'type' : type}})

    @staticmethod
    def delete_user(_id):
        mongo.db.users.delete_one({'_id':ObjectId(_id)})
