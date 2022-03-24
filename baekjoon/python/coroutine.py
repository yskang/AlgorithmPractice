from functools import wraps

def coroutine(func):
    @wraps(func)
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

def printer():
    while True:
        line = (yield)
        print(line)

prn = printer()
prn.send('hello world')