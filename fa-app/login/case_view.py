from login import app
from flask import render_template
from flask import request, redirect
import services.case_manger as cs

@app.route("/case",methods=["GET", "POST"])
def load_cases():
    if request.method == "POST":
        req = request.form
        print(req)
        cs.create_case(req)
        print("created case")
    return render_template("case.html")