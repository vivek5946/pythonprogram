# parent class
class animal:
    def speak(self):
        print('animal is speaking')
# child class


class lion(animal):
    def roar(self):
        print('lion is roaring')


simba = lion()
simba.roar()
print(dir(simba))
simba.speak()
# multilevel inheritance


class cub(lion):
    def walk(self):
        print('walking')


b = cub()
b.walk()
b.roar()
b.speak()

# multiple inheritance


class calc1:
    def addition(self, a, b):
        return a+b


class calc2:
    def multiplication(self, a, b):
        return a*b


class calc3(calc1, calc2):
    def subtraction(self, a, b):
        return a-b


a = calc3()
print(a.multiplication(5, 6))
print(a.subtraction(4, 3))
print(a.addition(3, 4))
print(issubclass(calc3, calc2))

print(isinstance(a, calc2))


class A:
    def mk(self):
        print('i am class A')


class B:
    def mk(self):
        print('i am class B')


class C(A, B):
    def __init__(self):
        print('class c getting constructed')


f = C()
f.mk()
# if function name same in both class then it will execute accrding to method resolution order
# first content of C will print then A
# method overriding-------------------


class D(A):
    def mk(self):
        print('i am from class D')


g = D()
g.mk()
# method overloading and operator overloading
# data abstraction ==> hide the data


class S:
    # to hide count from [user] put double underscore infront of it

    __count = 0

    def __init__(self):
        S.__count += 1

    def printcount(self):
        print('count is:', S.__count)


stud1 = S()
stud1.printcount()
# print(stud1.__count)
# you can not acesses this count like this because its abstract it will show error
