from login import app
from flask import render_template
from flask import request, redirect
import os
import services.case_manger as cs
import ast

app.config["IMAGE_UPLOADS"] ='./data/imgs'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]

@app.route("/photograph")
def load_photos():
    casw_ids = cs.get_case_ids()
    # group_ids = list(map(lambda x: str(x[0]),cs.get_group_info()))
    group_ids = cs.get_group_info()
    print(casw_ids, group_ids)
    return render_template("photograph2.html",cids = casw_ids ,gids = group_ids)


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

    print("got submit")
    req = request.form.to_dict()
    print(req)
    if request.method == "POST":

        photo_obj = {}
        photo_obj["cid"] = ast.literal_eval(req['case_id'])[0]
        photo_obj["case_id"] = ast.literal_eval(req['case_id'])[1]
        photo_obj["gid"] = ast.literal_eval(req['group_id'])[0]
        photo_obj["group_id"] = ast.literal_eval(req['group_id'])[1]
        photo_obj['photo_des'] = req["photo_des"]

        if request.files:
            print("file found",request.files)

            image = request.files["img"]
            ext = image.filename.rsplit(".", 1)[1]


            if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
                file_name = image.filename
                dir_path =os.path.join(app.config["IMAGE_UPLOADS"],str(photo_obj["group_id"]),str(photo_obj["cid"]))
                file_path = os.path.join(dir_path,file_name)
                photo_obj['file_path'] = str(file_path)
                photo_obj['file_name'] = str(file_name)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                image.save(file_path)
                print(photo_obj)
                cs.create_photo_path(photo_obj)
                print('------------------',file_path, "><" ,file_name)


            else:
                return render_template("photograph2.html")

            print("Image saved")
    return render_template("photograph2.html")
