import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        finished_time = time.time()
        print(f"{function.__name__} run speed: {finished_time - start_time} seconds")
    return wrapper_function()


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i + i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i + i
