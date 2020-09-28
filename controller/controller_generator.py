from .test_op import TestOp
from functools import wraps

def controller_generate(controller_class):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            controller = controller_class()
            return f(controller=controller, *args, **kwargs)
        return wrapped
    return decorator

test_controller_generator = controller_generate(TestOp)
