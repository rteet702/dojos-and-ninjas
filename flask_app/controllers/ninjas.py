from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja


@app.route('/ninjas')
def r_add_ninja():
    dojos = Dojo.get_all()
    return render_template('ninjas.html', dojos=dojos)

@app.route('/ninjas/add_ninja', methods=['POST'])
def f_add_ninja():
    inbound = request.form
    data = {
        'first_name': inbound['first_name'],
        'last_name': inbound['last_name'],
        'age': inbound['age'],
        'dojo' : inbound['dojo']
    }
    Ninja.add_ninja(data)
    return redirect('/dojos')

@app.route('/ninjas/<id>')
def r_update_ninja(id):
    data = {
        'id' : id
    }
    ninja = Ninja.get_one(data)
    dojos = Dojo.get_all()
    return render_template('edit_ninja.html', ninja=ninja, dojos=dojos)

@app.route('/ninjas/update', methods=['POST'])
def f_update_ninja():
    inbound = request.form
    data = {
        'id' : inbound['id'],
        'first_name': inbound['first_name'],
        'last_name': inbound['last_name'],
        'age': inbound['age'],
        'dojo' : inbound['dojo']
    }
    Ninja.update_ninja(data)
    return redirect('/dojos')

@app.route('/ninjas/<dojo_id>/<id>/delete')
def f_delete_ninja(dojo_id, id):
    data = {
        'id' : id
    }
    Ninja.delete_ninja(data)
    return redirect(f'/dojos/{dojo_id}')