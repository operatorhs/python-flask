from App.ext import db


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class User(db.Model):
    # __tablename__ = 'UserModel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(16), unique=True)
    u_des = db.Column(db.String(128), nullable=True)


class Animal(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(16))


class Dog(Animal):
    __talbename__ = 'AnimalModel'
    d_legs = db.Column(db.Integer, default=4)


class Cat(Animal):
    d_eat = db.Column(db.String(32), default='fish')


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    c_name = db.Column(db.String(16))

    addresses = db.relationship('Address', backref="customer", lazy=True)


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_position = db.Column(db.String(128))
    a_customer_id = db.Column(db.Integer, db.ForeignKey(Customer.id))


class Goods(BaseModel):

    g_name = db.Column(db.String(64))
    g_price = db.Column(db.Float, default=0)

