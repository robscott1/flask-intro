from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
	return 'Hello, world!'

@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
	if request.method == 'GET':
		print(request.args)
		search_username = request.args.get('name')
		search_job = request.args.get('job')

		if search_username and search_job :
			subdict = {'users_list' : []}
			for user in users['users_list']:
				if user['name'] == search_username and user['job'] == search_job:
					subdict['users_list'].append(user)
			return subdict

		elif search_username :
			subdict = {'users_list' : []}
			for user in users['users_list']:
				if user['name'] == search_username:
					subdict['users_list'].append(user)
			return subdict

		else:
			return users
	elif request.method == 'POST':
		userToAdd = request.get_json()
		users['users_list'].append(userToAdd)
		resp = jsonify(success=201)
		return resp
	elif request.method == 'DELETE':
		userToDelete = request.get_json()
		deleted = False
		lst = users['users_list']
		for user in lst:
			if user['id'] == userToDelete['id']:
				lst.remove(user)
				deleted = True
		resp = jsonify(success=True, deleted=deleted)
		return resp
   
			
