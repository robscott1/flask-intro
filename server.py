from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

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
		search_username = request.args.get('name')
		if search_username :
			subdict = {'users_list' : []}
			for user in users['users_list']:
				if user['name'] == search_username:
					subdict['users_list'].append(user)
			return subdict
		return users
	elif request.method == 'POST':
		userToAdd = request.get_json()
		users['users_list'].append(userToAdd)
		resp = jsonify(success=True)
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
   
			
