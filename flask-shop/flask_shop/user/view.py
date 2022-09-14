# -*- coding = utf-8 -*-
# @time : 2022/5/18 22:21
# @author : 李志
# @file : view.py
# @software : PyCharm



import re
from flask_shop.user import user, user_api
from flask_shop import models, db
from flask import request
from flask_restful import Resource, reqparse
from flask_shop.utils.message import to_get_status
from flask_shop.utils.token import generate_auth_token, verify_auth_token, login_required

# 创建注册路由接口 使用restful
class User(Resource):
    def get(self):
        try:
            id = int(request.args.get('id').strip())
            usr = models.User.query.filter_by(id = id).first()
            if usr:
                return to_get_status(200, usr.to_dict(), '获取用户成功')
            else:
                return to_get_status(1000, [], '没有此用户')

        except Exception as e:
            print(e)
            return to_get_status(2000)

    def post(self):
        # 获取用户传输的注册数据
        name = request.form.get("name")
        pwd = request.form.get("pwd")
        real_pwd = request.form.get("real_pwd")
        nick_name = request.form.get("nick_name")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # 验证是否符合格式规范和数据是否完整
        if not all([name, pwd, real_pwd]):
            return to_get_status(1000)
        if len(name)<2:
             return to_get_status(1001)
        if len(pwd)<2:
             return to_get_status(1002)
        if pwd!=real_pwd:
             return to_get_status(1003)
        # 正则匹配手机号和邮箱是否合法
        if not re.match(r"1[345678]\d{9}", phone):
             return to_get_status(1004)
        if not re.match(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$', email):
             return to_get_status(1005)
        # 将用户传输验证好的1数据保存数据库
        try:
            rid = int(request.form.get('role_name')) if request.form.get('role_name') else 0
            user = models.User(name=name, password=pwd, nick_name=nick_name, phone=phone, email= email, rid=rid)
            db.session.add(user)
            db.session.commit()
            return to_get_status(200, msg='注册成功')
        # 如果数据存在还回异常
        except Exception:
            return to_get_status(2000)

    def put(self):
        try:
            id  = int(request.form.get('id').strip())
            email = request.form.get('email').strip() if request.form.get('email') else ''
            phone = request.form.get('phone').strip() if request.form.get('phone') else ''
            rid = request.form.get('role_name')
            if rid:
                try:
                    rid = int(rid)
                except Exception as e:
                    rid = models.User.query.get(id).rid
            else:
                rid = models.User.query.get(id).rid
            
            usr = models.User.query.get(id)
            if usr:
                usr.email = email
                usr.phone = phone
                usr.rid = rid
                # db.session.add(usr)
                db.session.commit()
                return to_get_status(200,msg='修改数据成功！')
            else:
                return to_get_status(1008)
        except Exception as e:
            print(e)
            return to_get_status(1000)

    def delete(self):
        try:
            id  = request.json.get('id')
            usr = models.User.query.get(id)
            if usr:
                db.session.delete(usr)
                db.session.commit()
                return to_get_status(200,msg='删除成功！')
            else:
                return to_get_status(1009)
        except Exception as e:
            return to_get_status(2000)

# 注册api接口资源
user_api.add_resource(User, '/user')


class UserList(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',type=str)
        parser.add_argument('pnum',type=int)
        parser.add_argument('psize',type=int)
        try:
            args = parser.parse_args()
            name = args.get('name')
            pnum = args.get('pnum') if args.get('pnum') else 1
            psize = args.get('psize') if args.get('psize') else 2
            if name:
                users_p = models.User.query.filter(models.User.name.like(f'%{name}%')).paginate(pnum,psize)
            else:
                users_p = models.User.query.paginate(pnum,psize)
            data = {
                'pnum':pnum,
                'totalPage':users_p.total,
                'users':[u.to_dict() for u in  users_p.items]
            }
            return to_get_status(200,data,'获取用户列表成功！！')
        except Exception as e:
            print(e)
            return to_get_status(1000)

user_api.add_resource(UserList,'/user_list')



# 用于测试
@user.route("/")
def index():
    return "welcome blueprints this"


# 创建登入路由接口
@user.route("/login", methods=["POST"])
# @login_required
def login():
    name = request.form.get("name")
    pwd = request.form.get("pwd")

    if not all([name, pwd]):
        return to_get_status(1000)

    if len(name) > 1:
        user = models.User().query.filter_by(name = name).first()
        if user:
            if user.check_password(pwd):
                token = generate_auth_token(user.id, 1000)
                verify_auth_token(token)
                return to_get_status(200, data={'token':token})
                # return {'status':200, 'msg': '登入成功'}

    return to_get_status(1015)


# 创建登入路由接口
@user.route("/reset", methods=["GET"])
def reset():
    try:
        id = int(request.args.get('id'))
        usr = models.User.query.get(id)
        usr.password = '123'
        db.session.commit()
        return to_get_status(200, msg='重置密码成功')
    except Exception as e:
        return to_get_status(2000)