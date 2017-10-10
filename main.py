from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key ='random string'

@app.route('/')
def index():
	
	return render_template('signup.html')


@app.route('/', methods = ['POST', 'GET'])
def signup():

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		verify_ps = request.form['verify']
		email_address = request.form['email']
		
		#Create variables in session so that they can be used in ohter functions. 
		session['username'] = username
		session['email'] = email_address

		#Create string variables to store error messages.
		username_error =''
		password_error =''
		verify_error = ''
		email_error = ''
			
		#create integer variables to store the number of At and Dot.
		count_at = 0
		count_dot =0
		
		if len(username) < 3:
			username_error = "That's not a valid username"
		else:
			for chr in username:
				if chr == ' ':
					username_error = "That's not a valid username!"
		
		if len(password) == 0 :
			password_error = "That's not a valid password!"
			
		if len(verify_ps) == 0 or verify_ps != password :
			verify_error = " Passwords don't match!"
		
		if (2<len(email_address)<21):
			for i in email_address:
				if i =='@':
					count_at += 1
				elif i == '.':
					count_dot += 1
				elif i != ' ':
					email_error = "That's not a valid email!"
					break
		
		# if email_error == '':
			# if (count_at != 1 or count_dot != 1):
				# email_error = "You have entered an invalid email address!"
		
		if (username_error !=''or password_error !=''or verify_error!=''or email_error !=''):
			return render_template('signup.html', username = username, email = 'email', \
				username_error = username_error, password_error = password_error, \
				verify_error = verify_error, email_error = email_error)
		else:
			return render_template('welcome.html', username = username)
		
def welcome():
    	return render_template('welcome.html', username = username)



if __name__=='__main__':
	app.run()