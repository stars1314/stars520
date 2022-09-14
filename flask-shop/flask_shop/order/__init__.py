from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
order = Blueprint("order", __name__)
# 创建restful api接口对象
order_api = Api(order)

from flask_shop.order import view