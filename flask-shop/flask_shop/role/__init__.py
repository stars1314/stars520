from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
role = Blueprint("role", __name__)
# 创建restful api接口对象
role_api = Api(role)

from flask_shop.role import view