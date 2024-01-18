from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.modelDojo import Dojo
from flask_app.models.modelNinja import Ninja

#TODO
@app.route('/dojos')
def get_all_dojos():
    all_dojos = Dojo.get_all_dojo_m()
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/ninjas')
def get_allDojo():
    each_dojos = Dojo.get_all_dojo_m()
    return render_template('newNinja.html', each_dojos=each_dojos)

@app.post('/create_dojo')
def add_1_dojo():
    Dojo.add_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def display_dojo_ninjas(dojo_id):
    data = {
        'id': dojo_id
    }
    ninjas_by_dojo_id = Ninja.get_ninjas_by_dojo(data)                  #??
    citys_and_dojos = Dojo.get_one_dojo(data)   
    print(citys_and_dojos)         #??
    return render_template('dojoThenninja.html', ninjas_by_dojo_id=ninjas_by_dojo_id, citys_and_dojos=citys_and_dojos)

    


