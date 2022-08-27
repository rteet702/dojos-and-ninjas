from flask import redirect, render_template
from flask_app import app


@app.route('/dojos')
def dojos():
    return render_template('dojos.html')