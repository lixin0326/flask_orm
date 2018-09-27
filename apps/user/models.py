from apps.ext import db


class User(db.Model):
    # name 表示列名
    # __tablename__=''
    # index 索引
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    id_delete = db.Column(db.Boolean)
    price = db.Column(db.Numeric(7, 2))
    """
    重要参数
    argument 关联的类名
    uselist  一对一的关系 一对多必须是设置uselist=True
    backref  反向引用的名称
    lazy     懒加载
    """

    address_list = db.relationship('Address',
                                   uselist=True,
                                   backref='user',
                                   lazy='dynamic'
                                   )


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(100), nullable=False)
    detail = db.Column(db.Text)
    # 　建立外键字段 外键一定要在多的一方
    uid = db.Column(db.Integer, db.ForeignKey(User.uid))
