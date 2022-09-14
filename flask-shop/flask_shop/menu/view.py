from flask_shop.menu import menu, menu_api
from flask_shop import models, db
from flask import request
from flask_restful import Resource
from flask_shop.utils.message import to_get_status


class Menu(Resource):
    def get(self):
        type_ = request.args.get('type')
        menu_list = []
        if type_ == 'list':
            # 获取数据,并将数据填充到menu_list
            mu = models.Menu.query.filter(models.Menu.level != 0 ).all()
            for m in mu:
                # 将遍历得到的数据转成json数据保存到列表
                menu_list.append(m.to_dict())
        else:
            mu = models.Menu.query.filter(models.Menu.level == 1 ).all()
            for m in mu:
                # 获取1级菜单转成json
                first_mu = m.to_dict()
                # 给2级菜单创建保存容器
                first_mu['children'] = []
                for sm in m.children:
                    # 获取2级菜单转成json
                    second_dict = sm.to_dict()
                    # 给2级菜单创建保存容器，并把3级菜单数据加进来
                    second_dict['children'] = sm.get_child_list()
                    # 把2级单级菜单加到1级的chilren列表中
                    first_mu['children'].append(second_dict)
                # 把1级单级菜单加到根列表中
                menu_list.append(first_mu)
        return to_get_status(200,data=menu_list)

# 注册api接口资源
menu_api.add_resource(Menu, '/menu')