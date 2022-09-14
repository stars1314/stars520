from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
menu = Blueprint("menu", __name__)
# 创建restful api接口对象
menu_api = Api(menu)

from flask_shop.menu import view