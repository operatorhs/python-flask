import random
from App.ext import db
from flask import Blueprint, redirect, url_for, request, render_template, make_response, Response, abort, session
from werkzeug import security
import uuid

from App.models import Student, Cat, Dog, Customer, Address

blue = Blueprint('blue', __name__, template_folder='../templates')


def init_view(app):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return 'Index'

@blue.errorhandler(401)
def handelError(error):
    print(error)
    print(type(error))
    return 'What?'

@blue.route('/add_student')
def add_student():
   student = Student()
   student.name = '小花%d' % random.randrange(10000)

   db.session.add(student)
   db.session.commit()

   print(db.session)
   print(type(db.session))

   return '添加一个用户成功'


@blue.route('/add_students')
def add_students():
    students = []
    for i in range(5):
        student = Student()
        student.name = '小明%d' % i
        students.append(student)

    db.session.add_all(students)
    db.session.commit()
    return 'students ok'


@blue.route('/get_student')
def get_student():
    # student = Student.query.first()
    # student = Student.query.get_or_404(12)
    student = Student.query.get(1)
    return student.name


@blue.route('/get_students')
def get_students():
    students = Student.query.all()
    for student in students:
        print(student.name)
    return render_template('student_list.html', students=students)


@blue.route('/delete_student')
def delete_student():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()

    return 'Delete Success'


@blue.route('/update_student')
def update_student():
    student = Student.query.first()
    student.name = 'Tom'
    db.session.commit()

    return 'Update Success'


@blue.route('/add_cat')
def add_cat():
    cat = Cat()
    cat.a_name = '汤姆猫'
    cat.d_eat = '老鼠'

    db.session.add(cat)
    db.session.commit()

    return 'cat add ok'


@blue.route('/add_dog')
def add_dog():
    dog = Dog()
    dog.a_name = '傻狗'
    dog.d_legs = 5

    db.session.add(dog)
    db.session.commit()

    return 'dog ok'


@blue.route('/get_cats/')
def get_cats():
    cats = Cat.query.offset(1).limit(2)
    print(cats)
    return render_template('Cats.html', cats=cats)


@blue.route('/add_dogs')
def add_dogs():
    for i in range(20):
        dog = Dog()
        dog.a_name = '二哈%d' % random.randrange(1000)
        db.session.add(dog)

    db.session.commit()
    return '添加数据成功'


@blue.route('/get_dogs/')
def get_dogs():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 4, type=int)

    dogs = Dog.query.offset(per_page * (page - 1)).limit(per_page)
    return render_template('Dogs.html', dogs=dogs)


@blue.route('/get_dogs_paginate/')
def get_dogs_paginate():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 4, type=int)
    paginate = Dog.query.paginate(page=page, per_page=per_page)
    dogs = paginate.items
    total = paginate.total
    print(dogs)
    print(total)
    print(type(dogs))
    return render_template('Dogs.html', dogs=dogs)


@blue.route('/get_cats_by')
def get_cats_by():
    cats = Cat.query.filter_by(id=5)
    return '获取数据成功'


@blue.route('/add_customer')
def add_customer():
    customer = Customer()
    customer.c_name = '剁手党%d' % random.randrange(1000)
    db.session.add(customer)
    db.session.commit()
    return '添加地址成功'


@blue.route('/add_address')
def add_address():
    address = Address()
    address.a_position = '宝胜利%d' % random.randrange(10000)
    address.a_customer_id = Customer.query.order_by(-Customer.id).first().id

    db.session.add(address)
    db.session.commit()
    return '添加地址成功'
