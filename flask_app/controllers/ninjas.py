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