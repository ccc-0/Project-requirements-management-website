from flask import Flask,url_for,redirect,render_template,Blueprint
from user.views import user_bp
from flask import send_from_directory
from extensions import db #,login_manager


app = Flask(__name__)
app.config.from_object('settings.Config')

# 绑定扩展
# db.init_app(app)
app.app_context().push()
# login_manager.init_app(app)

# 注册蓝图
app.register_blueprint(user_bp,url_prefix='/user')
# app.register_blueprint(post_bp,url_prefix='/post')

# 定义全局错误处理函数
@app.errorhandler(404)
def error404(error):
    return "页面未找到",404


# @app.route('/')
# def hello_world():
#     return redirect(url_for('user.index'))

# @app.route('/media/<path:filename>')
# def media(filename):
#     return send_from_directory(app.config['UPLOAD_PATH'],
#                                filename=filename)



if __name__ == '__main__':
    app.run()
