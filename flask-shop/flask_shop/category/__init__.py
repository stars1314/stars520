from flask import Blueprint
from flask_restful import Api

# 创建蓝图接口对象
category = Blueprint("category", __name__)
# 创建restful api接口对象
category_api = Api(category)


# 创建蓝图接口对象
attribute = Blueprint("attribute", __name__, url_prefix='/category')
# 创建restful api接口对象
attribute_api = Api(attribute)

from flask_shop.category import view
