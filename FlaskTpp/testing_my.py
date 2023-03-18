import jwt

from jwt import PyJWTError
# import datetime
from datetime import datetime, timedelta

payload = {
    'user_id': 1,
    'exp': datetime.now() + timedelta(seconds=30)
}

screct_key = 'test'

token = jwt.encode(payload, key=screct_key, algorithm='HS256')
print(token)

try:
    data = jwt.decode(token, key=screct_key, algorithms='HS256')
    print(data)
    # t = datetime(datetime.now())
    print(datetime.now())
    print(datetime.fromtimestamp())

except PyJWTError as e:
    print('jwt 验证失败', e)


# print(datetime.utcnow())
# print(datetime.now())
