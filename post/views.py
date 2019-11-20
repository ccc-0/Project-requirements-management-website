from flask import  Blueprint,request,render_template,redirect,url_for,current_app
from post.form import *
from werkzeug.utils import secure_filename
import os
from models import user,db
from flask import  flash

post_bp = Blueprint('post',__name__,static_folder='static',template_folder='templates')

@post_bp.route("/登录页面")
def login():
    return render_template("登录页面.html")

@post_bp.route("/登录页面")
def login():
    return render_template("登录页面.html")

if __name__ == '__main__':
    user_bp.run()
