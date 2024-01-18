from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.modelUsers import User

@app.route('/users/new')
def user_new():
    return render_template('Register.html')

@app.post('/users/create')
def create_user():

    is_valid = User.validate(request.form)
    if not is_valid:
        return redirect('/')#TODO make sure to use the new_user or it wont work for html

    hash_password =  bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form, 
        'password' : hash_password
    }

    user_id = User.create(data)
    session['email'] = request.form['email']
    session['uuid'] = user_id
    print(session['email'])
    return redirect('/dashboard')



@app.route('/register', methods=['POST'])
def register():
    if not User.validate_user(request.form):    
        return redirect('/')  
    return redirect('/dashboard')

@app.post('/users/login/process')
def users_login_process():
    User.validate_login(request.form)
    return redirect('/')


