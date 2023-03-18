import hashlib


def email_hash(email):
    return hashlib.md5(email.encode('utf-8')).hexdigest()
