from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model import User
#restful routing
@app.route('/users/new')
def user_new():
    return render_template("create.html")

@app.route('/users/create', methods=["POST"])
def create():
    user_id = User.create_new(request.form)
    return redirect("/users")

@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template("read.html", users=users)

@app.route('/users/<int:id>')
def show_user(id):
    user = User.get_one_by_id(id)
    return render_template("showUsers.html", user=user)

@app.route('/users/<int:id>/edit' )
def user_edit(id):
    user = User.get_one_by_id(id)
    return render_template('edit.html',user=user)

@app.post("/users/saveEdit" )
def user_saveEdit():
    User.update_users(request.form)
    redirect('/users')
    
@app.route("/delete/<int:id>")
def user_delete(id):
    User.user_delete(id)
    return redirect('/users')





# /Tablename/id?/action
# 1. /tablename/new -> Display \\ Displaying the form to create a new row
# 2. /tablename/create -> Redirect \\ Processing the data from the form from the new route
# 3. /tablename/id -> Display \\ Show route, this route displays the SINGLE ITEM with the id
# 4. /tablename/id/edit -> Display \\ This is a display route that shows the form to edit the row information
# 5. /tablename/id/update -> Redirect \\ The route that processes the form from the edit route
# 6. /tablename/id/delete -> Redirect \\ This is the route that 
# 7. /tablename/id/delete/confirm -> Redirect \\ Confirms if the user wants to delete