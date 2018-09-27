import datetime
from flask import Blueprint
from sqlalchemy import and_, or_, func

from apps.ext import db
from .models import User

user = Blueprint('user', __name__)


@user.route('/')
def index():
    return 'hello'


@user.route('/login/', methods=['post', 'get', 'head', 'put', 'delete'])
def login():
    User.query.all()
    return '登陆'


@user.route('/user/add/')
def add():
    # test = User(username='雪慧', password='123', price=5.20)
    # 保存单个对象
    # db.session.add(test)
    # db.session.commit()
    users = []
    for i in range(1, 11):
        users.append(User(username=f'test{i}', password=12345, price=666))
    db.session.add_all(users)
    return '添加数据'


@user.route('/user/find/')
def find():
    users = User.query.all()
    user = User.query.get(1)
    return '查询成功!'


@user.route('/user/find1/')
def find1():
    # User.query.all()

    # User.query.filter_by(username='雪慧')
    # User.query.filter(User.username.ilike('%1%'))  # .ignore忽略大小写
    # User.query.filter(User.username.like('%1%'))
    # 　in操作
    # User.query.filter(User.age.in_([]))
    #  not in操作
    # User.query.filter(~User.age.in_([]))
    # query = User.query.filter(and_(User.username == '', User.password == ''))
    # User.query.filter(
    #     or_(User.username.ilike('%t%'),
    #         User.age == 18,
    #         User.create_date < datetime.datetime.now())).order_by(User.username)
    #
    # User.quety.filter(User.age.between(10, 20))

    """
    分页查询
    第一页 0-10 size
          11-20

    limit   每次取多少条
    offset  从多少条开始(起始值)
    """
    # users = User.query.limit(10).offset(0).all()
    # print(len(users))
    users = User.query.order_by(User.uid).limit(10).offset(0).all()

    # User.query.order_by(User.uid).pagation()

    # 　分组查询　with_entities

    # with_entities 过滤列
    # django values() [{key:值}] values_list()
    # select username password from user
    # user = User.query.with_entities(User.username,User.password).first()

    # count max min avg
    # select age sum(uid) from user group by age
    sum = User.query.with_entities(User.age,
                                   func.sum(User.uid),
                                   func.max(User.uid),
                                   func.avg(User.uid)
                                   )

    return '查询信息'


@user.route('/user/update/')
def update():
    # user = User.query.get(1)
    # user.username = '小媳妇呀'

    # User.query.filter(User.uid == 1).update({User.password: '456'})

    # 批量更新 如果是批量更新必须设置Flase 否则是fetch
    User.query.filter(User.username.ilike('%t%')).update({User.price: 66}, synchronize_session=False)
    return '修改成功!'


# 查询用户信息以及用户的地址信息
@user.route('/user/list/')
def list():
    user = User.query.get(1)
    for address in user.address_list:
        print(address)
    return '关联查询'
