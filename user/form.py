from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError,Regexp,EqualTo,Email
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed,FileRequired

class CreateUserForm(FlaskForm):
    # user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    # account = db.Column(db.String, unique=True, nullable=False)
    # role = db.Column(db.Enum(0,1,2,3),nullable = False, default=1)
    # password = db.Column(db.String, nullable=False)
    # is_active = db.Column(db.Boolean, default=True, nullable=False)
    # sex = db.Column(db.Enum("男","女"),defailt="男" ,nullable = True)
    # userphoto = db.Column(db.String(50))  # 路径  ,default='默认.pnf'

    user_id = StringField("用户id",validators=[DataRequired()])
    account =  StringField('账号',
                           validators=[DataRequired(message="name不能为空"),Regexp(r'^.[a-z][a-zA-Z0-9_]{4,13}$')])
    role = BooleanField(label="是否活跃")
    password = PasswordField('密码',validators=[Length(min=6),DataRequired(),Regexp(r'^[a-z0-9_-]{6,18}$')])
    is_active = BooleanField(label="是否活跃")
    sex = BooleanField(label="是否活跃")
    userphoto = FileField(label="上传头像")

