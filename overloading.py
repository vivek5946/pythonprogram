# we can use same method for different functionality
# we can use same  operator for different meaning
# method overloading
class A:
    def mycalculate(self, x=None, y=None):
        if x != None and y != None:
            return x+y
        elif x != None:
            return x**2
        else:
            return 0


res = A()
print('zero argument passed', res.mycalculate())
print('one argument passed', res.mycalculate(5))
print('two argument passed', res.mycalculate(9, 5))


# 0perator overloading--------------------------------------------------
# operator overloading has built in function with double underscore
class B:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __eq__(self, other):
        if self.num == other.num:
            return "both are equal"
        else:
            return 'not equal'


obj1 = B(2)
obj2 = B(3)
print('addition by operator overloading:', obj1+obj2)
print(obj1 == obj2)
