import sys


for i in [1, 8, 2, "python"]:  # in--> membership operator
    print("hello")
print("program ends")
a = [100, 2, 3, 56]
print(100 in a)
# not also membership operator
print(100 not in a)
if 200 not in a:
    print("not available")
# identity operator
m = 100
n = 200
print(m == n)  # or you can use following
print(m is n)
print(m is not n)
# is operator not only check values they also check memory adress
s = 100
t = 100
print(s is t)  # ans shoulid be true but it will print false
# it is happining becasuse id of s and t means adresses are difference
print(id(s))
print(id(t))
a = [1, 2, 3]
for i in a:
    print(i**2)  # i**2 means i squre
for j in "python":
    print(j)
# range function
print(list(range(10)))
print(tuple(range(4, 20)))  # it will go till 19
print(tuple(range(1, 50, 2)))  # it will go from 1 to 50 and increment by 2
for i in range(1, 10):
    print("hi"*i)  # here we are asking print hi i times
for i in range(10):
    print(i, end=" ")
print(end="\n")
# every input in python is string hence you have to convert it into numerical

a = int(input("enter the value of a:"))

b = int(input("enter the value of b:"))
if a < b:
    print("hello")
else:
    print("a is not big")

if a < b:
    print("hello")
elif a == b:
    print("a is not big")
elif a < b:
    print("a is small")
while a < b:
    print("hello")
    a = a+1
a = [1, 5, 2, 8, 7]
# we want op like this b=[1,25,4,64,49]
b = list()
for i in a:
    b.append(i**2)
print(b)
print([i**2 for i in a if i % 2 == 0])  # this is called as list comprehension
e = [i for i in "python"]
print(e)
l = list()
for i in 'python':
    for j in "learn":
        l.append(i+j)
print(l)
# we are going to take input from above list
f = []
for k in l:
    f.append(k[1])
print(f)
# or you can write like this
v = [i[-1] for i in l]  # this called as list comprehension
print(v)
# tuple comprehension ==> generators
# generators==>low memory consumption
# g is generator and it is printed by list or for loop or next(g)
g = (i**2 for i in range(5))
# next(g) will print only one value from generator at time
next(g)
print(list(g))
print(dir(sys))
# example for size difference between list and generators
v = [i for i in range(100000)]  # list
x = (i for i in range(100000))  # generator
print(sys.getsizeof(v))
print(sys.getsizeof(x))
# -----------Dictionary comprehension----------
a = ["tom", "python", "sam"]
b = {}  # dictionary
for i in a:
    b[i] = len(i)
print(b)
# comprehension
m = {i: len(i)for i in a}
print(m)
b = [85, 98, 91]
d = ["chennai", "mum", "bang"]
c = []
for i in range(len(b)):
    c.append((a[i], b[i], d[i]))
print(c)
# ----------zip function----
# it is used to merge two or more list
print(list(zip(a, b)))
print(tuple(zip(a, b)))
