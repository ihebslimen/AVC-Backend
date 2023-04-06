from flask import Flask, request, jsonify
from flask_pymongo import PyMongo , ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

# set up Flask app
app = Flask(__name__)

# set up MongoDB client and database

app.config['MONGO_URI']= 'mongodb+srv://iheb:iheb@cluster0.bjpaw5n.mongodb.net/supplychain?retryWrites=true&w=majority'
mongo = PyMongo(app)
# define routes
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        # get all users
        users = mongo.db.users.find()
        user_list = []
        for user in users:
            user['_id'] = str(user['_id'])
            user_list.append(user)
        return jsonify(user_list)
    elif request.method == 'POST':
        # create new user
        user = request.json
        user['password'] = generate_password_hash(user['password'] )
        result = mongo.db.users.insert_one(user)
        user['_id'] = str(result.inserted_id)
        return jsonify(user)

@app.route('/api/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        # get single user by ID
        user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user)
        else:
            return 'User not found', 404
    elif request.method == 'PUT':
        # update user by ID
        updated_user = request.json
        result = mongo.db.users.replace_one({'_id': ObjectId(user_id)}, updated_user)
        if result.modified_count == 1:
            updated_user['_id'] = user_id
            return jsonify(updated_user)
        else:
            return 'User not found', 404
    elif request.method == 'DELETE':
        # delete user by ID
        result = mongo.db.users.delete_one({'_id': ObjectId(user_id)})
        if result.deleted_count == 1:
            return '', 204
        else:
            return 'User not found', 404

# run app
if __name__ == '__main__':
    app.run(port=5000,debug=True)