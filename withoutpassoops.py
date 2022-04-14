class student:
    "This is student class we are learning class concept"
    # constructor in python defined by ---init-- function
    # insted of self you can use any thing
    # python sending one argument by default that we are collecting in self
    # we can use it as generic argument like template in c++
    # it is same like template we can use same argument for multiple function call
    # it is same like this pointer
    studentcount = 0  # class variable

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        student.studentcount += 1

    def printdetails(self):  # if you are writing method in class of python then then you have to write 'self'keyword as argument at first otherwise your method will not work
        print("hi", 'hello')

    def printname(self):
        print('name of student is', self.name)

    def printcount(self):
        print('no of student', student.studentcount)


# instance==object
stud1 = student('rajesh', 'CSE')  # stud1 is object
stud2 = student('jui', 'IT')
print(stud1.printdetails())
stud1.printname()
stud2.printname()
print(dir(stud1))  # directory of object
print('_'*50)
print(dir(student))  # directory of class
stud1.printcount()
