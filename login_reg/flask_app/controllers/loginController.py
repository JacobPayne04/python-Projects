from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.modelUsers import User

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    
    return render_template('Register.html')

@app.route('/dashboard')
def dashboard():
    if not 'uuid' in session:
        return redirect('/')
    dict = {
        'email' : session['email']
    }

    user = User.get_one_by_email(dict)
    return render_template('Welcome.html', user=user)


@app.route('/user/logout')
def logout_user():
    del session['uuid']
    return redirect('/')
    