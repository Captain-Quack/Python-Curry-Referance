from functools import partial, reduce
from operator import *
def curry(f):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= f.__code__.co_argcount:
            return f(*args, **kwargs)
        return partial(curried, *args, **kwargs)
    return curried

def value_of(curried_f):
    while hasattr(curried_f, 'func'):
        if hasattr(curried_f, 'args'):
            curried_f = curried_f.func(*curried_f.args, **curried_f.keywords)
        else:
            curried_f = curried_f()
    return curried_f
