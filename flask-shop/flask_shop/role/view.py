from flask_shop.role import role,role_api
from flask_shop import models,db
from flask import request
from flask_restful import Resource
from flask_shop.utils.message import to_get_status


class Role(Resource):
    def get(self):
        role_list = []
        try:
            roles = models.Role.query.all()
            role_list = [r.to_dict() for r in roles]
            return to_get_status(200, role_list,'获取角色列表成功！！')
        except Exception as e:
            return to_get_status(2000)
    
    def post(self):
        name = request.form.get('name')
        desc = request.form.get('desc')
        try:
            if name:
                role =models.Role(name =name ,desc = desc)
                db.session.add(role)
                db.session.commit()
                return to_get_status(200,msg='增加角色成功！！')
            return to_get_status(1000)
        except Exception as e:
            print(e)
            return to_get_status(2000)

    def delete(self):
        try:
            id = int(request.form.get('id'))
            r = models.Role.query.get(id)
            if r: # 是否找到？
                db.session.delete(r)
                db.session.commit()
                return to_get_status(200,msg='删除角色成功！！')
            return to_get_status(1000)
        except Exception as e:
            return to_get_status(2000)
    def put(self):
        try:
            id = int(request.form.get('id'))
            name =request.form.get('name').strip() if request.form.get('name') else ''
            desc =request.form.get('desc').strip() if request.form.get('desc') else ''
            if name:
                r = models.Role.query.get(id)
                if r:
                    r.name = name
                    r.desc = desc
                    db.session.commit()
                    return to_get_status(200,msg='修改角色信息成功！！！')
                return to_get_status(1010)
            return to_get_status(1000)
        except Exception as e:
            return to_get_status(2000)
      

role_api.add_resource(Role, '/role')

@role.route('/del_menu/<int:rid>/<int:mid>')
def del_menu(rid,mid):
    try:
        r = models.Role.query.get(rid)
        m = models.Menu.query.get(mid)
        if all([r,m]):
            if m in r.menus:
                r.menus.remove(m)
                if m.level ==1:
                    for temp_m in m.children:   # 获取删除当前根节点所有子节点
                        if temp_m in r.menus:   # 判断当前子节点是在当前权限
                            r.menus.remove(temp_m)
                db.session.commit()
                return to_get_status(200,data=r.get_menu_dict(),msg='删除权限成功！')
            return to_get_status(1011)
        return to_get_status(1000)
    except Exception as e:
        print(e)
        return to_get_status(2000)

@role.route('/set_menu/<int:rid>',methods=['POST'])
def set_menu(rid):
    try:
        role = models.Role.query.get(rid)
        mids = request.form.get('mids')
        if role:
            role.menus = []
            for m in mids.split(','):
                if m:
                    temp_menu = models.Menu.query.get(int(m))
                    if temp_menu:
                        role.menus.append(temp_menu)
            db.session.commit()
            return to_get_status(200,msg='分配权限成功！！')
        return to_get_status(1010)
    except Exception as e:
        print(e)
        return to_get_status(2000)