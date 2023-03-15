import time
from functools import wraps



def timeit(func):
    """ccc"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """这是timeit 装饰器"""
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print('used:', end-start)
        return ret
    return wrapper()


@timeit
def foo():
    """这是foo, 被装饰函数"""
    print('info')

