from datetime import  datetime
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from extensions import db

class User(db.Model,UserMixin):
    user_id = db.Column(db.Integer,autoincrement =True, primary_key = True,nullable = False)
    account = db.Column(db.String, unique =True,nullable = False)
    # role = db.Column(db.Enum(0,1,2,3),nullable = False, default=1)
    password = db.Column(db.String,nullable = False)
    is_active = db.Column(db.Boolean,default=True,nullable = False )
    # sex = db.Column(db.Enum("男","女"),defailt="男" ,nullable = True)
    userphoto = db.Column(db.String(50))#路径  ,default='默认.pnf'

    __tablename__= 'user'

class Need_info(db.Model):
    need_id = db.Column(db.Integer,autoincrement =True, primary_key = True,nullable = False)
    # user_id = db.Column(db.Integer,db.ForeignKey('user.user_id'))
    user_id = db.relationship("user",backref="user_id")
    project_name = db.Column(db.String,)
    need_content = db.Column(db.String,nullable= False)
    need_affirm = db.Column(db.Integer,nullable= False,default=0)
    # project_time  项目周期
    # project_offer 项目报价

    __tablename__ = 'need_info'

class Comment_info(db.Model):
    comment_id = db.Column(db.Integer,autoincrement =True, primary_key = True,nullable = False)
    # user_id =  db.Column(db.Integer,db.ForeignKey('user_id'),nullable = False)
    user_id = db.relationship("user",backref="user_id")
    # need_id = db.Column(db.Integer,db.ForeignKey('need_info.need_id'),nullable = False)
    need_id = db.relationship("need_info",backref="need_id")
    comment_content =db.Column(db.String,nullable = False,default ="")
    comment_time = db.Column(db.DateTime,default=datetime.now)

    __tablename__ = 'comment_info'

#     def set_password(self, password):
#         # self.password = password
#         self.password = generate_password_hash(password)
#
#     def check_password(self, password):
#         # if password==self.password :
#         #     return True
#         # else:
#         #     return False
#         return check_password_hash(self.password, password)
#
#
# def createSuperUser():
#     user = User(account="admin", password='admin', username='admin', email="98@qq.com", is_admin="True")
#     user.set_password('admin')
#     db.session.add(user)
#     db.session.commit()


