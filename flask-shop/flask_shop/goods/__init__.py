from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
goods = Blueprint("goods", __name__)
# 创建restful api接口对象
goods_api = Api(goods)

from flask_shop.goods import view