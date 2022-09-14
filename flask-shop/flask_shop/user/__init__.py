# -*- coding = utf-8 -*-
# @time : 2022/5/18 22:18
# @author : 李志
# @file : __init__.py.py
# @software : PyCharm


from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
user = Blueprint("user", __name__, url_prefix="/user")
# 创建restful api接口对象
user_api = Api(user)

from flask_shop.user import view