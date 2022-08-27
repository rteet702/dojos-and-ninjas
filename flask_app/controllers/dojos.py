from flask import redirect, render_template
from flask_app import app
from flask_app.models.dojos import Dojo


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)