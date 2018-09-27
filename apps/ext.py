from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def init_db(app):
    config_db(app)
    db.init_app(app)
    migrate.init_app(app=app, db=db)


def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 　设置请求结束之后自动提交 就不需要commit了
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
