
from flask import Blueprint, render_template, request
from exts import db

from apps.goods.models import Goods, UserGoods
from apps.user.models import User

goods_bp = Blueprint('goods', __name__, url_prefix='/goods')


# 用户找商品 (xxx用户购买了那些商品)
@goods_bp.route('/find_goods')
def find_goods():
    user_id = request.args.get('uid')
    user = User.query.get(user_id)
    print(user)
    return render_template('goods/find_goods.html', user=user)


# 商品找用户 （这个商品被那些用户购买了）
@goods_bp.route('/find_user')
def find_user():
    goods_id = request.args.get('gid')
    goods = Goods.query.get(goods_id)

    return render_template('goods/find_user.html', goods=goods)


# 用户购买商品
@goods_bp.route('/show')
def show():
    users = User.query.filter(User.isdelete==False).all()
    goods_list = Goods.query.all()
    return render_template('goods/show.html', users=users, goods_list=goods_list)


@goods_bp.route('/buy')
def buy():
    user_id = request.args.get('uid')
    goods_id = request.args.get('gid')

    ug = UserGoods()
    ug.user_id = user_id
    ug.goods_id = goods_id
    ug.number = 1
    db.session.add(ug)
    db.session.commit()

    return '购买商品'
