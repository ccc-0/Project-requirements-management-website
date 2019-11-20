import  os

class Config(object):
    # 项目配置
    SECRET_KEY = "dsfsfesjhken32r2fz"
    SQLALCHEMY_DATABASE_URI = "mysql://root:c5210308@127.0.0.1:3306/xiangmuguanli"
    UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'media')