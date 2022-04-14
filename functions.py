def my_func1():
    print("vivek")


my_func1()
print("-"*50)
for i in range(5):
    my_func1()
print("!"*50)
a = my_func1  # it will refer id of function means address
print(id(my_func1))
a()


def my_func2():
    return("hi")


print(my_func2())
# ------------


def func4(x, y):
    z = input("enter the value of Z:")
    if z.isnumeric():
        return x+y+int(z)
    else:
        print("z should be int")


a = func4(2, 5)
print(a)
# ---default arguments


def my_func6(x, y, z=True):
    while z:
        print(x+y)


c = my_func6(1, 2, False)
print(c)  # it will print "none"
# arbitrary arguments==> it used for adding more no of arguments


def my_func8(*signal):
    return sum(signal)


signal_strength = my_func8(3, 4, 6, 8, 90)
print(signal_strength)


def my_func9(**kw):
    print(type(kw))
    print(kw.values())


a = my_func9(x=10, y=20, c=50, d=2.5)
print(a)
