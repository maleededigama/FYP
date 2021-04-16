from login import app
from flask import render_template
from flask import request, redirect
import services.admin_services as ad
import services.case_manger as cs

@app.route("/group")
def group_load():
    students = ad.get_students()
    return render_template('group.html',ids=students)

@app.route("/group_create", methods=["GET", "POST"])
def create_group():
    if request.method == "POST":
        req = request.form
        print(req)
        ad.create_group(req)
    return render_template('group.html')


@app.route('/set_feedback')
def load_feedback():
    group_ids = cs.get_group_info()
    casw_ids = cs.get_case_ids()
    grades = ad.get_greades()
    return render_template('admin_feedback.html',cids = casw_ids ,gids = group_ids,grds=grades)

@app.route("/create_feedback", methods=["GET", "POST"])
def create_feedback():
    if request.method == "POST":
        req = request.form.to_dict()
        print(req)
        ad.create_feedback(req)
    return render_template('admin_feedback.html')