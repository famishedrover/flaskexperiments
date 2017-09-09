from flask import Flask , redirect , url_for , request, render_template

app = Flask (__name__)


@app.route('/')
def home_page():
	return render_template('login.html')

@app.route('/name/<user>/')
def hello_user(user):
	return render_template('hello.html',name=user)


@app.route('/success/<name>')
def success(name):
	return 'Welcome %s'%name

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST' :
		user = request.form['nm']
		print url_for('success',name=user)
		return redirect(url_for('success',name=user))
	else :
		user = request.args.get('nm')
		print url_for('success',name=user)
		return redirect(url_for('success',name=user))

if __name__ == "__main__" :
	app.run(host = '0.0.0.0',port=5000, threaded =True)