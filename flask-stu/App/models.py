from App.ext import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16))

    def save(self):
        db.session(self)
        db.commit()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20))
    s_password = db.Column(db.String(256))

