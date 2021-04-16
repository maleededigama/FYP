from flask import Flask


app = Flask(__name__)

# from login import myview
from login import login_view
from login import case_view
from login import photograph_view
from login import user_view
from login import admin_views
from login import form_view