from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
import string
from mongodb import User


app = Flask(__name__)

#CORS stands for Cross Origin Requests.
CORS(app) # Not recommended for production environment.

users = { 
    'users_list' :
    [
        {  
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123',            
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',            
            'name': 'Mac',
            'job': 'Professor',
        },        
        {
            'id' : 'yat999',            
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
             'id' : 'zap555',           
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    db = User()
    if request.method == 'GET':
        search_username = request.args.get('name')
        search_job = request.args.get('job')
        if search_username and search_job:
            
			# TODO: Replace with database access
            users = db.find_all()
            return find_users_by_name_job(search_username, search_job, users)
			# Done, uses db to get dictionary,
			# passes dict to edited fn that 
			# loops through users_list

        elif search_username:

            # using list shorthand for filtering the list.
            # TODO: Replace with database access
            result = User.find_by_name(search_username)
			# Done, use db method.

        else:
            result = User().find_all()
        return {"users_list": result}
    elif request.method == 'POST':
        userToAdd = request.get_json() # no need to generate an id ourselves
        newUser = User(userToAdd)
        newUser.save() # pymongo gives the record an "_id" field automatically
        resp = jsonify(newUser), 201
        return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        user = User({"_id":id})
        if user.reload() :
            return user
        else :
            return jsonify({"error": "User not found"}), 404
    elif request.method == 'DELETE':
        user = User({"_id":id})
        resp = user.remove()

        # TODO: Check the resp object if the removal was successful or not.
        # Return a 404 status code if it was not successful

		if resp['nRemoved'] != 0:
        	return {}, 204
		else:
			return {}, 404

def find_users_by_name_job(name, job, users):
    subdict = {'users_list' : []}
    for user in users:
        if user['name'] == name and user['job'] == job:
            subdict['users_list'].append(user)
    return subdict  