from flask import Flask , redirect , url_for 
#  importing this is mandatory.
# takes current module name as arg.
app = Flask(__name__)

# acts as a decorator which tells the application 
# which URL should call the associated function.
@app.route('/hello/<miss>')
def hello_world(miss):
	return 'Hello World '+miss

@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog Number: '+str(postID)

@app.route('/rev/<float:revNo>')
def devision(revNo):
	return 'Revision Number %f'%revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

# canonical URL by appending '/' at the end
# therefore can be accessed by both /python and /python/
@app.route('/python/')
def hello_python():
   return 'Hello Python'

@app.route('/admin/')
def hello_admin():
	return "'sup Admin !"

@app.route('/guest/<guest>/')
def hello_guest(guest):
	return 'Hi %s'%guest

@app.route('/user/<name>/')
def hello_user(name):
	if name =='admin':
		return redirect(url_for('hello_admin'))
	else :
		return redirect(url_for('hello_guest',guest=name))

@app.route('/getjson')
def getjson():
	return {{'key1':'one','key2':'two'}}
if __name__ == "__main__":
	app.run(host = '0.0.0.0')