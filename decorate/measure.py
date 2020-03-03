"""Module for measurements of function performances."""
import time


def call_counter(fn):
    """
    A decorator that stores how many 
    time the decorated function was called 
    in decorated_function_name.calls.
    """
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return fn

    wrapper.calls = 0
    return wrapper


def timing(fn):
    """
    A decorator that times the decorated 
    function and outputs the result.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fn(*args, **kwargs)
        print("Time taken by function {s}: {f}".format(
            __name__, time.time() - start_time))

    return wrapper
