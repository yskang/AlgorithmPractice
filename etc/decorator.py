import datetime
import time
from functools import wraps

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before execution of {} function".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_1():
    print("display_1 function is executed")


@decorator_function
def display_info(name, age):
    print("display_info({}, {}) function is executed".format(name, age))


class DecoratorClass:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Before execute {} function.".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display():
    print("display function is executed")


@DecoratorClass
def display_information(name, age):
    print("display_information({}, {}) is executed".format(name, age))


def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info("[{}] result args - {}, kwargs - {}".format(timestamp, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("total execute time of function {}: {} seconds".format(original_function.__name__, t2))
        return result
    return wrapper

@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print("displya_info({}, {}) is executed!!".format(name, age))

if __name__ == "__main__":
    display_info("hh", 33)

