from flask import session, g
from models.user import UserModel


def bbs_before_request():
    if 'user_id' in session:
        user_id = session.get('user_id')
        try:
            user = UserModel.query.get(user_id)
            setattr(g, 'user', user)
        except Exception:
            pass
