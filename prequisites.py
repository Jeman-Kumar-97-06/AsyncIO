from functools import wraps
def decorator1(og_func):
    def wrapper():
        return og_func()
    return wrapper

def display():
    print("display shit!")

decorator1_ = decorator1(display)
print(decorator1)
decorator1_()


def f1():
    return print('jeman')

f1()
print(f1.__name__)

def func1():
    import time
    print(time)
func1()


def decorator_1(og):
    @wraps(og)
    def nigga(*args,**kwargs):
        print("Ran Wrapper")
        return og(*args,**kwargs)
    return nigga

@decorator_1
def f(name,age):
    print("name",name,'\n',"age",age)

# f = decorator_1(f)
f('jeman',30)
print(f.__name__)