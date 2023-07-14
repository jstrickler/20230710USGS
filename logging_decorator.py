import logging
from functools import wraps

FUNCTION_LIST = []

def register(func):
    FUNCTION_LIST.append(func)
    return func


logging.basicConfig(
    filename="deco.log",
    level=logging.INFO,
    format="%(name)s %(levelname)s %(asctime)s %(message)s",
    datefmt="%x-%X",
)
logger = logging.getLogger()

def logfunction(func):

    @wraps(func)
    def replacement(*args, **kwargs):
        # function call time
        logger.info(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return replacement

@register
@register
@logfunction
def spam():
    print("SPAM SPAM SPAM")
# spam = logfunction(spam)

# register_function(spam)

@logfunction
def ham(x, y):
    return x * y + y / x

# ham = logfunction(ham)
@register
def toast():
    print("MMMMmm toasty toast")


spam()
print(ham(5, 10))
spam()
spam()
print(ham(10, 4.3))
print()
for function in FUNCTION_LIST:
    function()
print()

print(spam.__name__)
print(ham.__name__)

def pancakes():
    print("pancakes!!")

foo = logfunction(pancakes)

pancakes()

foo()

"""
@mydeco(x, y, z)
def myfunction():
    pass
    
myfunction = mydeco(x, y, z)(myfunction)

"""




