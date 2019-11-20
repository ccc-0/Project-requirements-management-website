from flask import  Blueprint,request,render_template,redirect,url_for,current_app
from user.form import *
from werkzeug.utils import secure_filename
import os
from models import User,Need_info,Comment_info,db
from flask import  flash

user_bp = Blueprint('user',__name__,static_folder='static',template_folder='templates')


@user_bp.route("/登录页面")
def login():
    return render_template("登录页面.html")

@user_bp.route("/软件开发者_当前需求")
def developer_demand():
    return render_template("软件开发者_当前需求.html")

@user_bp.route('/项目管理者_当前需求')
def pmanager_demand():
    return render_template("项目管理者_当前需求.html")

@user_bp.route('/软件客户_新增需求')
def client_newdemand():
    return render_template("软件客户_新增需求.html")

@user_bp.route('/未通过需求')
def np_damand():
    return render_template("未通过需求.html")

@user_bp.route('/已通过需求')
def ap_damand():
    return render_template("已通过需求.html")

@user_bp.route('/个人信息')
def person_info():
    return render_template("个人信息.html")

@user_bp.route('/关于我们')
def self_info():
    return render_template("关于我们.html")

@user_bp.route('/软件开发者需求详情')
def developer_d_info():
    return render_template("软件开发者需求详情.html")

@user_bp.route('/项目管理者需求详情')
def pmanager_d_info():
    return render_template("项目管理者需求详情.html")

@user_bp.route('/软件客户需求详情')
def client_d_info():
    return render_template("软件客户需求详情.html")


