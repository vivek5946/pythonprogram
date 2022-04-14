f = open("test.txt", "w")
print(id(f))
# f.close()
# f=open("Downloads",mode="w" encoding="utf-8")
print(dir(f))
f.write("gaurav is good programmer")
f.write("python is his favourite")
f.close()
# if we open it in write mode again it will overwrite hence we have to open it using append mode
f = open("test.txt", "w")

f.write("\n welcome to python\n")
f.write("weather is good\n")
f.close()
f = open("test.txt", "a")
f.write("\n vivek is a good person\n")
f.write("he is doing hardwork\n")
f.close()
# only when close the file then only data will go from buffer to file
f = open("test.txt", "r")

print(f.read())
print(f.tell())  # it will tell you which byte cursor is pointing to
f.seek(4)  # it will take your cursor to 4th byte
print(f.read())
f.close()
# to avoid using close ==>you can use with keyword
# "with "keyword file will close and open auttomatically
with open("test.txt", "w") as f:
    f.write("rajiv\n")
    f.write("jui\n")
# uppacking
# it contains list contain list and list contain tuple
# list contain iterarors


def my_func6(x, y):
    return x+y, x*y


a = my_func6(2, 3)
print(a)
# unpack
a, b = my_func6(2, 3)
print(a)  # it will print 5
print(b)  # it will print 6
# if you no of arguments for returns then you can write that many variables for connecting
