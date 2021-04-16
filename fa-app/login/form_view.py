from login import app
from flask import render_template
from flask import request, redirect

@app.route("/util_forms")
def load_fms():
    return render_template("forms.html")