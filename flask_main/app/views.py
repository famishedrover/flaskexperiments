from app import app
from flask import render_template, flash , redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Mudit'}
	posts = [
		{
			'author':{'nickname':'Rishi'},
			'body':'Never Give Up!'
		},
		{
			'author':{'nickname':'Robin'},
			'body':'Be Awesome.'
		}
	]

	return render_template('index.html',user = user,posts = posts)


@app.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit() :
		flash("Login Requested For OpenID=%s, remember_me=%s"%(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
		
	return render_template('login.html', 
						title='Log In',
						form=form,
						providers = app.config['OPENID_PROVIDERS'])
	





