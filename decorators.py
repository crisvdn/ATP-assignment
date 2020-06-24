import time

# calculate_time :: func
def calculate_time(func):
    """
    decorator that measures time in a specific function
    :param func: function to call
    :return:
    """
    def inner1(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time(seconds) taken in: ", func.__name__, format(end - begin, '.12g'))
    return inner1