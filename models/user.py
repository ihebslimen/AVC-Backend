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
            if user['role']== 'user':
                result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'] ,'state' : user['state'],'public_key' : user['public_key'],'private_key' : user['private_key']})
            elif user['role']== 'admin':
                result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'public_key' : user['public_key'],'private_key' : user['private_key']})

        return result

    @staticmethod
    def get_one_user(_id):
        user = mongo.db.users.find_one({'_id': ObjectId(_id)})
        if user['role']== 'user':
            result=  {'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'],'state' : user['state'],'public_key' : user['public_key'],'private_key' : user['private_key']}
        elif user['role']== 'admin':
            result = {'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'public_key' : user['public_key'],'private_key' : user['private_key']}

        return result
        
    @staticmethod
    def filter_users(query):
        users = mongo.db.users.find(query)
        result = []
        for user in users:
            if user['role']== 'user':
                result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'type' : user['type'],'state' : user['state'],'public_key' : user['public_key'],'private_key' : user['private_key']})
            elif user['role']== 'admin':
                result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role']),'public_key' : user['public_key'],'private_key' : user['private_key']})

        return result
    @staticmethod
    def create_user(cin, name, email, phone, role, state, type ='', actorInfoJson = ''):
        filter_result = User.filter_users({'cin':cin})
        if filter_result:
            return "User already signed up"
        
        keys = Actor.generate_key_pair()
        if role == 'admin':
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role,"public_key": keys['public_key'],"private_key" : keys['private_key']}
            res = mongo.db.users.insert_one(user)
        elif role == 'user':
            user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role, 'type' : type,'state': state,"public_key": keys['public_key'],"private_key" : keys['private_key'] }
            user_id = mongo.db.users.insert_one(user).inserted_id
            actorInfoJson['user_ref'] = user_id
            res = mongo.db[type].insert_one(actorInfoJson)
        if res.acknowledged :
            return 'succeed'
        else:
            return 'failed'


    @staticmethod
    def update_user(_id , query):
        user = mongo.db.users.find_one({'_id': ObjectId(_id)})

        forbiddenQueriesAdmin = ['_id','role', 'cin' , 'public_key.txt' , 'private_key','state' , 'type'  ]
        forbiddenQueriesUser = ['_id','role', 'cin' , 'public_key.txt' , 'private_key' ]
        if user['role'] == 'admin':
            for fq in forbiddenQueriesAdmin :
                if fq in query:
                    return f"Unable to update {fq} attribute"
        elif user['role'] == 'user' : 
            for fq in forbiddenQueriesUser:
                if fq in query:
                    return f"Unable to update {fq} attribute"
                    
        res = mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': query})
        if res.acknowledged :
            result =  'updated'
        else : 
            result =  'not updated'

        return result
    
    @staticmethod
    def delete_user(_id):
        res = mongo.db.users.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
