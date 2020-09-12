# decorators.py
import time
from functools import wraps

def square(n):
    return n ** 2

def timer(func):
    decorator ='timer'
    @wraps(func)
    def timed(*args):
        start = time.time()
        return {
            "time": time.time()-start, 
            "return": func(*args),
            "func": func.__name__,
            "decorator": decorator
        }

    return timed


print(square(2))

timed_square = timer(square)
print(timed_square(2))