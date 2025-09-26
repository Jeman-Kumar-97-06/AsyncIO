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