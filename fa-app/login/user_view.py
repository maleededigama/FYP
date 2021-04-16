from login import app
from flask import render_template
from flask import request, redirect
from services.user_verification import UserAct


@app.route("/user",methods=["GET", "POST"])
def user_profile():
    ua = UserAct()
    if request.method == "POST":
        req = request.form
        print(req)
        ua.create_user(req)


    return render_template("user.html")