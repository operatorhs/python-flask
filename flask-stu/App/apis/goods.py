from flask import request
from flask_restful import Resource, abort, fields, marshal_with, marshal, reqparse
from App.models import Goods


goods_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='g_name'),
    'g_price': fields.Float
    # 'uri': fields.Url('sign_goods', absolute=True)
}

single_goods_fields = {
    'data': fields.Nested(goods_fields),
    'status': fields.Integer,
    'msg': fields.String
}


multi_goods_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(goods_fields)),
    'desc': fields.String(default='success')
}

# 获取参数校验
parser = reqparse.RequestParser()
# parser.add_argument('g_name', type=str, help='please input g_name', required=True)
parser.add_argument('g_price', type=float)
parser.add_argument('mu', action='append')
parser.add_argument('rname', dest='name')  # 取别名
parser.add_argument('csrftoken', location='cookies')


class GoodsListResource(Resource):

    @marshal_with(multi_goods_fields)
    def get(self):
        goods_list = Goods.query.all()
        args = parser.parse_args()
        print('这边测试args', args.get('csrftoken'))
        data = {
            'status': 200,
            'msg': 'ok',
            'data': goods_list
        }
        return data

    # @marshal_with(goods_fields)
    @marshal_with(single_goods_fields)
    def post(self):
        # g_name = request.form.get('g_name')
        # g_price = request.form.get('g_price')
        args = parser.parse_args()
        g_name = args.get('g_name')
        g_price = args.get('g_price')
        name = args.get('name')
        print(name)

        mu = args.get('mu')
        print(mu)

        goods = Goods(g_name=g_name, g_price=g_price)
        goods.save()

        if not goods.save():
            abort(400)

        data = {
            'msg': 'create success',
            'status': 200,
            # 'data': marshal(goods, goods_fields)
            'data': goods
        }
        # return goods
        return data


class GoodsResource(Resource):
    @marshal_with(single_goods_fields)
    def get(self, id):
        goods = Goods.query.get(id)
        data = {
            'status': 200,
            'msg': 'ok',
            'data': goods
        }
        return data

    def delete(self, id):
        goods = Goods.query.get(id)
        if not goods:
            # abort(404)
            abort(404, message='goods doesn')
        if not goods.delete():
            abort(400)
        data = {
            'msg': 'delete success',
            'status': 204
        }
        return data

    @marshal_with(single_goods_fields)
    def put(self, id):
        goods = Goods.query.get(id)
        if not goods:
            abort(404)
        g_price = request.form.get('g_price')
        g_name = request.form.get('g_name')
        goods.g_name = g_name
        goods.g_price = g_price

        if not goods.save():
            abort(400)
        else:
            data = {
               'msg': 'message put ok',
               'status': 201,
               'data': goods
            }
            return data

    @marshal_with(single_goods_fields)
    def patch(self, id):
        goods = Goods.query.get(id)
        if not goods:
            abort(404)
        g_price = request.form.get('g_price')
        g_name = request.form.get('g_name')
        goods.g_name = g_name or goods.g_name
        goods.g_price = g_price or goods.g_price

        if not goods.save():
            abort(400)
        else:
            data = {
               'msg': 'message put ok',
               'status': 201,
               'data': goods
            }
            return data
