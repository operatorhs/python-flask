from flask import Blueprint, redirect, url_for, request
from werkzeug import security
import uuid

blue = Blueprint('blue', __name__)


def init_view(app):
    app.register_blueprint(blue)


@blue.route('/user/<int:id>', methods=['GET', 'POST'])
def user(id):
    print(id)
    print(type(id))
    return 'UserID %d' % id


@blue.route('/user/<string:token>/')
@blue.route('/user/<int:token>')
def token(token):
    print('获得token')
    return f'token {token}'


@blue.route('/get_path/<path:address>/')
def get_path(address):
    print(uuid.uuid4())
    return f'address { address }'


@blue.route('/getuuid/<uuid:uid>')
def get_uuid(uid):
    return f'uuid {uid}'


@blue.route('/getany/<any(a, b):an>/')
def get_any(an):
    print(an)
    print(type(an))
    return 'Any success'


@blue.route('/red')
def redirect_my():
    return redirect(url_for('blue.get_any', an='a'))


@blue.route('/request', methods=['GET', 'POST', 'PUT'])
def get_request():
    print(request.host)
    print(request.remote_addr)
    print(request.remote_user)
    if request.method == 'GET':
        return 'GET Success'
    elif request.method == 'POST':
        return 'POST Success'
    else:
        return f'{request.method} Not Support'


@blue.route('/')
def index():
    return 'Index'

