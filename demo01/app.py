from flask import Flask, current_app, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, desc, func

app = Flask(__name__)

app.config['ENV'] = 'development'


HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'hs6307609'
DATABASE = 'database_learn'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:hs6307609@127.0.0.1:3306/database_learn'


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


db = SQLAlchemy(app)


# with db.engine.connect() as conn:
#     rs = conn.execute('select 1')
#     print(rs.fetchone())

# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# print(a)
# ctx.pop()

# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']
#     print(a, d)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

    articles = db.relationship('Article', back_populates='author')
    extension = db.relationship('UserExtension', back_populates='user', uselist=False)


class UserExtension(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    school = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), unique=True)
    user = db.relationship('User', back_populates='extension')


article_tag_table = db.Table(
    'article_tag_table',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    password = db.Column(db.Text, nullable=False)
    # content = db.Column(db.Text, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey(User.id))
    author = db.relationship('User', back_populates='articles')
    tags = db.relationship('Tag', secondary=article_tag_table, back_populates='articles')


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200))
    articles = db.relationship('Article', secondary=article_tag_table, back_populates='tags')


@app.route('/many2many')
def many2may():
    user = User.query.first()
    article1 = Article(title='11333', password='33332', author=user)
    article2 = Article(title='2dsadf2', password='bb233', author=user)

    tag1 = Tag(name='python')
    tag2 = Tag(name='flask')

    article1.tags.append(tag1)
    article1.tags.append(tag2)
    article2.tags.append(tag1)
    article2.tags.append(tag2)

    db.session.add_all([article1, article2])
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.add(tag1)
    # db.session.add(tag2)

    db.session.commit()

    return '多对多数据添加成功'


@app.route('/article/add')
def article_add():
    user = User.query.first()
    article = Article(title='aa', password='ccc', author=user)
    db.session.add(article)
    db.session.commit()

    return '添加数据成功'


@app.route('/fetch_article')
def fetch_article():
    articles = Article.query.all()
    for article in articles:
        # print(article.tags)
        for tag in article.tags:
            print('===>', tag.name)
    return render_template('article.html', articles=articles)


@app.route('/one2one')
def one2one():
    user = User.query.first()
    user2 = User.query.get(2)
    extension1 = UserExtension(school='清华大学', user=user)
    extension2 = UserExtension(school='北京大学', user=user2)
    db.session.add(extension1)
    db.session.add(extension2)
    db.session.commit()
    return '添加成功'


@app.route('/user/add')
def user_add():
    user1 = User(username='张三2', password='111')
    user2 = User(username='李四3', password='222')
    user3 = User(username='王五4', password='333')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()
    return '用户添加成功'


@app.route('/user/fetch')
def user_fetch():
    users = User.query.all()
    # user = User.query.get(1)
    # user = User.query.get(2)
    # user = User.query.first()
    user = User.query.get(1)
    print(User.query.exists())
    print(User.query.count())
    # user = User.query.one_or_one()
    return render_template('index.html', users=users, user=user)


@app.route('/user/filter')
def user_filter():
    user = User.query.get(2)
    # users = User.query.filter_by(username='张三')
    # users = User.query.filter(User.username=='张三')
    # users = User.query.slice(2,4)
    # users = User.query.offset(3).limit(3)
    # users = User.query.order_by(User.password.desc())
    # users = User.query.order_by(desc('password'))
    # users = db.session.query(User.password, func.count(User.id).label('password_count')).group_by('password').all()

    # users = User.query.filter(User.username.contains('张'))
    # users = User.query.filter(User.username.like('%张%'))
    users = User.query.filter(User.username.in_(['张三', '李四', '王五']))

    return render_template('index.html', users=users, user=user)


with app.app_context():
    db.create_all()

    with db.engine.connect() as conn:
        # conn = db.engine.connect()
        rs = conn.execute(text('select 1'))
        print(rs.fetchone())


if __name__ == '__main__':
    app.run(debug=True)
