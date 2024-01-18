from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.modelNinja import Ninja
from flask_app.models.modelDojo import Dojo

@app.route('/ninjas')
def get_all_ninjas():
    all_ninjas = Ninja.get_all()
    return render_template('dojos.html', all_ninjas=all_ninjas)

@app.post('/create/ninja')
def add_1_ninja():
    Ninja.add_new_ninja(request.form)
    return redirect('/ninjas')














# /Tablename/id?/action
# 1. /tablename/new -> Display \\ Displaying the form to create a new row
# 2. /tablename/create -> Redirect \\ Processing the data from the form from the new route
# 3. /tablename/id -> Display \\ Show route, this route displays the SINGLE ITEM with the id
# 4. /tablename/id/edit -> Display \\ This is a display route that shows the form to edit the row information
# 5. /tablename/id/update -> Redirect \\ The route that processes the form from the edit route
# 6. /tablename/id/delete -> Redirect \\ This is the route that 
# 7. /tablename/id/delete/confirm -> Redirect \\ Confirms if the user wants to delete