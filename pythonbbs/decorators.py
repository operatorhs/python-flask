from functools import wraps
from flask import g, redirect, url_for


def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if not hasattr(g, 'user'):
            return redirect(url_for('user.login'))
        else:
            return func(*args, **kwargs)
    return inner

