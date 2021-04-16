from login import app
from flask import render_template
from flask import request, redirect
from services.user_verification import User

#
@app.route("/", methods=["GET", "POST"])
def index():
    print(request.form)
    user = User()
    if request.method == "POST":
        req = request.form
        pw = req['inputPassword']
        email = req['inputEmailAddress']
        if user.check_user_pw(pw,email) and True:
            return redirect('/base')

    return render_template("login.html")

@app.route("/home")
def home():
    print("Dashboard is rendering ")
    return render_template('dashboard.html')

@app.route("/base")
def base():
    print("Dashboard is rendering ")
    return render_template('base.html')


#
#
