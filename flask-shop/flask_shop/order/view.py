from flask_shop.order import order, order_api
from flask_shop import models, db
from flask import request
from flask_restful import Resource
from flask_shop.utils.message import to_get_status


@order.route('/order_list')
def order_list():
    id = request.args.get('id')
    if id:
        order = models.Order.query.get(id)
        if order:
            return to_get_status(200, order.to_dict(), '获取订单成功')
        else:
            return to_get_status(1012)

    orders = models.Order.query.all()
    return to_get_status(200, [o.to_dict() for o in orders], '获取订单列表成功！！')


@order.route('/express')
def get_express():
    oid = request.args.get('oid')
    if oid:
        exps = models.Express.query.filter(models.Express.oid == oid).order_by(models.Express.update_time.desc())
        return to_get_status(200, [e.to_dict() for e in exps])
    else:
        return to_get_status(1000)
