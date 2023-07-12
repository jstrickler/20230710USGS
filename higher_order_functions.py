import operator as op

def doit(func):
    func()
    return func

def hello():
    print("Hello, USGS world")

f = doit(hello)

f()

print(f"f is hello: {f is hello}")


x = doit(lambda : print("woo hooooooo"))

x()

def add(x, y):
    return x + y

print(f"add(5, 10): {add(5, 10)}")
print(f"op.add(5, 10): {op.add(5, 10)}")
print('-' * 60)

print(dir(op))
