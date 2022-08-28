from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/add_dojo', methods=['POST'])
def add_dojo():
    inbound = request.form
    data = {
        "name" : inbound['dojo_name']
    }
    Dojo.add_dojo(data)

    return redirect('/dojos')

@app.route('/dojos/<id>')
def show_dojo(id):
    data = {
        "id" : id
    }
    dojo = Dojo.get_one(data)
    ninjas = Ninja.get_by_dojo(data)
    return render_template('dojo_info.html', dojo=dojo, ninjas=ninjas)

@app.route('/dojos/<id>/edit')
def r_edit_dojo(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    return render_template('edit_dojo.html', dojo=dojo)

@app.route('/dojos/edit', methods=['POST'])
def f_edit_dojo():
    inbound = request.form
    dojo_id = inbound['id']
    data = {
        'id': dojo_id,
        'name': inbound['name']
    }
    Dojo.edit_dojo(data)
    return redirect(f'/dojos/{dojo_id}')