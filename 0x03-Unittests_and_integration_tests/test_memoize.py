from time import perf_counter
from functools import wraps
from typing import Callable

def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method."""
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return property(memoized)

class MyClass:
    def __init__(self):
        self.counter = 0

    @memoize
    def expensive_method(self):
        print("Computing a costly result...")
        self.counter += 1
        return self.counter

my_object2 = MyClass()
start = perf_counter()
print(my_object2.expensive_method)
done = perf_counter()
print(done-start)
start = perf_counter()
print(my_object2.expensive_method)  # Returns the cached result, no recomputation
print(my_object2._expensive_method)
done = perf_counter()
print(done - start)
