a = []  # empty list  and list supports all data type
type(a)  # list is mutable array
print(type(a))
print("hello")
a.append(1)
print(a)
a.append("vivek")  # append takes only one argument at time
print(a)
c = "hello"
c.upper()
print(c)
print(c.upper())
c = c.upper()
print(c)
b = [100, "hi", 200, 67.75]  # directly created list
print(b)
# ----------indexing------------
print(a[0])
print(b[1])
print(b[-1])
# ------slicing----
b[0:2]
print(b[0:2])
d = b[::-1]  # this method is used for reversing list

print(b[::-1])  # it will print reverse list
print(b[-3:-1])  # it will print values from end
# value at -1(last) and value at -3(from last)
b[0] = 1000
print(dir(list))  # it will print all directories present in python
n = b.pop()  # it will pop last element of list
print(n)
print(b)
b.pop(1)  # it will remove element at index 1
# to add multiple element to list use extend function
a.extend([100, 150, 7.8])
print(a)
a.append([89, 100, 2.5])  # it will create nested list
print(a)
print(b[-1])
print(a[-1])
print(a[-1][0])
print(a[-1][-1])  # it will go list of inside list and print last element
a[-1].append("python")
print(a[-1])
print(a[-1][-1])
print(a[-1][-1][-1])  # it will print "n"
a.insert(2, 2500)  # it will add 2500 at second position
a.count(2500)  # it will give us how many occurences of 2500 in list
# it will count occurences of outer list not nested list
a.remove(2500)  # it will remove 2500

print(a)
a.remove(7.8)
print(a[-1].index("python"))
a.remove(150)  # it will remove occuurence of 150
print(a)
# -------sort will accept only numerical values
# sorting will happen in ascending order by default
b.extend([2.5, 80, 100, 2])
b.sort()  # it will print in ascending order
print(b.sort(reverse=True))
# it will print in decending order
# clear all element on list
b.clear()
print(b)
# copy function
d = a.copy()
print(id(d))
# ----------------------TUPLE-------------------
m = (1, 2.5, 35, "hi", 2899)
print(type(m))
print(m[0])
# m[0]=100 we cant write like this because it is non mutable
print(dir(tuple))
# ---type conversion and type casting
# List to tuple
print(a)
tuple(a)
print(type(a))
a = list(a)
print(type(a))
# -------dictionary--------------------------
my_dict = {}
print(type(my_dict))
my_dict["name"] = "ton"
print(my_dict)
my_dict["age"] = 22
print(my_dict)
stud_rec = {"name": ["sam", "john", "jack"],
            "age": [21, 22], "city": ["baglore"]*3}
print(stud_rec)
print(stud_rec.keys())
print(stud_rec.values())
my_set = {1, 2, 3, 4, 5, "hello", 2232, 1, 8}
print(type(my_set))
print(my_set)  # it will not print indexing
# my_set[0]=2 you cant write like this because its dose not support indexing
print(dir(set))
my_set.pop()  # it will remove random value
my_set.remove(2232)
print(my_set)
engg = [1101, 1108, 1105, 1109, 1204]
mang = [1501, 1101, 1306, 1204, 1617]
print(set(engg).intersection(set(mang)))
print(list(engg).intersection(set(mang)))
