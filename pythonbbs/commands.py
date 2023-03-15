import click
from ext import db
from models.post import BoardModel, PostModel
from faker import Faker
import random

from models.user import PermissionEnum, PermissionModel, RoleModel, UserModel
# celery -A app.celery worker -l info 去定celery


def my_command():
    click.echo('这是我自定义的命令')


def create_permission():
    for permission_name in dir(PermissionEnum):
        if permission_name.startswith('__'):
            continue
        permission = PermissionModel(name=getattr(PermissionEnum, permission_name))
        db.session.add(permission)
    db.session.commit()

    click.echo('权限添加成功')


def create_role():
    inspector = RoleModel(name='稽查', desc='负责审核帖子和评论是否合法合规')
    inspector.permissions = PermissionModel.query.filter(PermissionModel.name.in_([
        PermissionEnum.POST,
        PermissionEnum.COMMENT
    ])).all()

    operator = RoleModel(name='运营', desc='负责网站持续正常运营')
    operator.permissions = PermissionModel.query.filter(PermissionModel.name.in_([
        PermissionEnum.POST,
        PermissionEnum.COMMENT,
        PermissionEnum.BOARD,
        PermissionEnum.FRONT_USER,
        PermissionEnum.CMS_USER
    ])).all()

    administrator = RoleModel(name='管理员', desc='负责整个网站的所有工作！')
    administrator.permissions = PermissionModel.query.all()

    db.session.add_all([inspector, operator, administrator])
    db.session.commit()
    click.echo('角色添加成功')


def create_test_user():
    admin_role = RoleModel.query.filter_by(name='管理员').first()
    zhangsan = UserModel(username='张三', email='zhangsan@zlkt.net', password='123456', is_staff=True, role=admin_role)

    operator_role = RoleModel.query.filter_by(name='运营').first()
    lisi = UserModel(username='李四', email='lisi@zlkt.net', password='123456', is_staff=True, role=operator_role)

    inspector_role = RoleModel.query.filter_by(name='稽查').first()
    wangwu = UserModel(username='王五', email='wangwu@zlkt.net', password='123456', is_staff=True, role=inspector_role)

    db.session.add_all([zhangsan, lisi, wangwu])
    db.session.commit()
    click.echo('测试用户添加成功')


@click.option('--username', '-u')
@click.option('--email', '-e')
@click.option('--password', '-p')
def create_admin(username, email, password):
    admin_role = RoleModel.query.filter_by(name='管理员').first()
    admin_user = UserModel(username=username, email=email, password=password, is_stff=True, role=admin_role)
    db.session.add(admin_user)
    db.session.commit()
    click.echo('管理员创建成功')


def create_board():
    board_names = ['python语法', 'web开发', '数据分析', '测试开发', '运维开发']
    for board_name in board_names:
        board = BoardModel(name=board_name)
        db.session.add(board)
    db.session.commit()
    click.echo('板块添加成功')


# 生成测试数据
def create_test_post():
    fake = Faker(locale='Zh_CN')
    author = UserModel.query.get('kyrprg9RtJpJ8TSyEL2AbY')
    boards = BoardModel.query.all()

    click.echo('开始生成帖子...')
    for x in range(98):
        title = fake.sentence()
        content = fake.paragraph(nb_sentences=10)
        random_index = random.randint(0, 4)
        board = boards[random_index]
        post = PostModel(title=title, content=content, board=board, author=author)
        db.session.add(post)
    db.session.commit()
    click.echo('测试帖子生成成功')
