from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojos import Dojo


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
