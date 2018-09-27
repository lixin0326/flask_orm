from flask import Flask
from apps.ext import init_db
from apps.user.views import user


# 程序的入口
def create_app():
    app = Flask(__name__)
    # 开发者模式debug设置
    app.debug = True
    # 蓝图注册
    register_blue(app)
    # 数据库注册
    init_db(app)

    return app


def register_blue(app):
    app.register_blueprint(user)
