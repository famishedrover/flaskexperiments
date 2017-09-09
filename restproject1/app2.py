from flask import Flask,url_for, request, Response, jsonify
import json

from functools import wraps

app = Flask(__name__)

@app.route('/')
def api_root():
	return 'Welcome'

@app.route('/articles')
def api_articles():
	return 'List of '+url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
	return 'You are reading '+articleid

@app.route('/hello')
def api_hello():
	print request.args
	if 'name' in request.args:
		return 'Hello'+request.args.get('name')
	else :
		return 'Hi Person of Earth.'

@app.route('/hello2',methods=['GET'])
def api_hello2():
	data = {
		'hello':'world',
		'number':3
	}
	js = json.dumps(data)
	# resp = Response(js,status =200, mimetype='application/json')
	resp = jsonify(data)
	resp.status_code = 200
	resp.headers['Link'] = 'http://google.com'
	return resp




@app.route('/messages', methods=['POST'])
def api_message():
	if request.headers.get('Content-type') == 'text/plain':
		return 'Text Message '+request.data

	elif request.headers.get('Content-type') == 'application/json':
		return 'JSON MESSAGE '+json.dumps(request.json)
	elif request.headers.get('Content-type') == 'application/octet-stream':
		f = open('.binary','wb')
		f.write(request.data)
		f.close()
		return 'Binary Message Written'
	else :
		'415 Unsupported Media Type.'



@app.errorhandler(404)
def not_found(error=None):
	message = {
		'status':404,
		'message':'Not Found: '+request.url
	}
	resp = jsonify(message)
	resp.status_code = 404
	return resp
	

@app.route('/users/<userid>',methods=['GET'])
def api_users(userid):
	users = {
		'1':'Mudit',
		'2':'Robin',
		'3':'Xander'
	}
	if userid in users:
		return jsonify({userid:users[userid]})
	else:
		return not_found()



# authorization
def check_auth(username,password):
	return username=='admin' and password =='admin'
def authenticate():
	message = {'message':'Authenticate.'}
	resp = jsonify(message)
	resp.status_code = 401

	resp.headers['Owener'] = 'Mudit Verma'
	return resp
def requires_auth(f):
	@wraps(f)
	def decorated(*args,**kwargs):
		auth = request.authorization
		# print auth
		if not auth :
			return authenticate()
		elif not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args,**kwargs)
	return decorated


@app.route('/secret')
@requires_auth
def api_secret():
	print request
	return 'Secret Revealed.'


if __name__ == '__main__' :
	app.run(host='0.0.0.0',debug=True)











