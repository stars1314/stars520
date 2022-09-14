# -*- coding = utf-8 -*-
# @time : 2022/5/18 21:47
# @author : 李志
# @file : __init__.py
# @software : PyCharm



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_map

# 创建数据库对象
db = SQLAlchemy()


def create_app(config_name):
    # 创建一个Flask对象
    app = Flask(__name__)
    # 得到运行模式，生产或者开发
    obj = config_map.get(config_name)
    # 加入配置参数
    app.config.from_object(obj)
    # 将app对象初始化到数据库
    db.init_app(app)

    # 注册蓝图
    from flask_shop.user import user
    app.register_blueprint(user)
    
    # 注册蓝图
    from flask_shop.menu import menu
    app.register_blueprint(menu)

    # 注册蓝图
    from flask_shop.role import role
    app.register_blueprint(role)

    # 注册蓝图
    from flask_shop.category import category
    app.register_blueprint(category)

    # 注册蓝图
    from flask_shop.category import attribute
    app.register_blueprint(attribute)

    # 注册蓝图
    from flask_shop.goods import goods
    app.register_blueprint(goods)

    # 注册蓝图
    from flask_shop.order import order
    app.register_blueprint(order)
    
    # 还回app对象
    return app
