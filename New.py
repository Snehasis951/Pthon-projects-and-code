'''def function(a, b):
    # """This is a function which will calculate average of two numbers"""
    # average = (a+b)/2
    # return average
x = function(10, 12)
print(x)
print(function.__doc__)'''

'''n1 = input("enter the first number: ")
n2 = input("enter the second number: ")
try:
    print("the sum of two number is: ", int(n1) + int(n2))
except Exception as e:
    print(e)

print("boom!")'''

#File IO basics  
'''r mode = open file for reading default mode
w mode = open file for writing 
x mode= create file if not existing 
a mode = addd more content to a file
t mode = text mode default mode
b mode = binary mode 
+ mode = read and write'''

# file writing
'''f = open("py.txt", "r")
content = f.read(5)
print(content)
f.close()'''

'''f = open("py.txt", "rt")
for line in f:
    print(line)
f.close()'''

'''f = open("py.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(10)
print(f.readline())
# print(f.tell())
f.close()'''

'''with open("py.txt") as f:
    a = f.read(16)
    print(a)'''

'''l = 10  # Global variable
def func1(n):
    # l = 5 #Local variable
    global l  #for providing permission in order to change global varible
    m = 10
    print(l, m)
    print(n, "printed")
func1("this is me")
print(l)'''

'''x = 25
def snehasis():
    x = 23
    def annesha():
        global x
        x = 36
    # print("before calling annesha()", x)
    annesha()
    print("after calling annesha()", x)
snehasis()
print(x)'''

#iterative method for collecting factorial of a number21
'''def factorial(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac
number = int(input("enter the number: "))
print(factorial(number))'''

#recursion method for collecting factorial of a number 
'''def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("enter the number: "))
print(factorial(number))'''

# fibonacci number
# 0 1 1 2 3 5 8 13.....
'''def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
number = int(input("enter the number: "))
print(fibonacci(number))'''

# sorting list according to 2nd elements
'''def a_first(x):
    return x[1]
x = [[1, 5], [45, 3], [12, 15]]
x.sort(key=a_first)
print(x)'''


# sorting list according to 2nd elements with the help of lambda function
'''x = [[1, 5], [45, 3], [12, 15]]
x.sort(key=lambda x:x[1])
print(x)'''

# F string 
'''import math
me = "snehasis"
sm = 23
ar = f"this is {me} {sm} {23 * 36} {math.cos(30)}"
print(ar)'''

# *args and **kwargs
#method 1
'''def funargs(*args): #args has helped to execute tuple from arguments
    print(args[2])

x = ["snehasis", "annesha", "mondal", "roy"]
funargs(*x)'''

#method 2 using for loop
'''def funargs(normal, *args, **kwargs): #args has helped to execute tuple from arguments
    print(normal)
    for item in args:
        print(item)
    print("\nPresenting our new generation AI and Automation heros")
    for key, value in kwargs.items():
        print(f"{key} is the {value}")
x = ["snehasis", "annesha", "mondal", "roy"]
y = {"Snehasis":"web developer and AI specialist", "Annesha": "automation specialist and software developer"}
normal = "it is a normal argument"
funargs(normal, *x, **y)'''

# time module 
# comparing for loop and while loop run time and the run time is almost similar in both the cases
'''import time
initial = time.time()
print(initial)
k = 0
while (k<36):
    print("ALU")
    k+= 1
print("while loop ran in", time.time() - initial, "seconds")
initial2 = time.time()
for i in range(36):
    print("ALU")
print("for loop ran in", time.time() - initial2, "seconds")'''

# localtime
'''import time
localtime  = time.asctime(time.localtime(time.time())) 
# asctime has helped to change time tuple to a representable time 
# localtime has helped to find time in a tuple format
print(localtime)'''


# Enumerate Function
'''list = ["potato", "onion", "chowmin", "mango"]
for index, item in enumerate(list):
    if index%2 == 0:
        print(f"JARVIS buy {item}")'''

# importaing working procedure in python
'''import sys
print(sys.path)'''

# join function 
'''list = ["a", "b", "c", "d", "e"]

# for item in list:
    # print(item, "and", end=" ")
a = " , ".join(list)
print(a, "other names")'''

# map function
# example 1
'''nos = ["4", "6", "8"]
nos = list(map(int, nos))

# for i in range(len(nos)):
    # nos[i] = int(nos[i])
nos[2] = nos[2] + 4
# print(nos[2])'''
# example 2
'''def sq(x):
    return x*x
nos2 = [1,2,3,4,5,6,7,8,9,10]
squarenos = list(map(sq, nos2))
print(squarenos)'''
# example 3
'''def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
number = [1,2,3,4,5,6,7,8,9,10]
for i in range(8):
    value = list(map(lambda x:x(i), func))
    print(value)'''

# filter function
'''number = [1,2,3,4,5,6,7,8,9,10]
def is_grater_6(num):
    return num>6
gr_than_6 = list(filter(is_grater_6, number))
print(gr_than_6)'''

# reduce function 
'''from functools import reduce
number = [1,2,3,4,5,6,7,8,9,10]
nos = reduce(lambda x, y: x+y, number)
print(nos)'''

# Decorators In Python
# def func(num):
    # if num == 0:
        # return print
    # if num == 1:
        # return int
    # if num == 2:
        # return sum
# a = func(2)
# print(a)

'''def dec(func1):
    def nowexec():
        print("executing now")
        func1()
        print("execueted")
    return nowexec
@dec
def who_is_snehasis():
    print("Snehasis is great footballer")
who_is_snehasis()'''

# OOPS
# Classes - Template
# Object - Instance Of the Class
# DRY - Do not repeat Yourself

# OOPS class
'''class student:
    pass

Snehasis = student()
Annesha = student()

Snehasis.name = "Snehasis"
Snehasis.std = "Graduate"
Snehasis.CGPA = 8.44
Annesha.name = "Snehasis"
Annesha.std = "Graduate"
Annesha.CGPA = 8.49
print(Snehasis.std)
print(Annesha.CGPA)'''

#OOPS Instance & Class Variables 
'''class Employee:
    no_of_leaves = 10
    pass

Snehasis = Employee()
Annesha = Employee()

Snehasis.name = "Snehasis"
Snehasis.salary = 650000
Snehasis.role = "AI specialist and web developer"

Annesha.name = "Annesha"
Annesha.salary = 550000
Annesha.role = "Software developer"
Annesha.no_of_leaves = 12

print(Snehasis.no_of_leaves)
print(Annesha.__dict__)
print(Employee.__dict__)'''

# Self & __init__() (Constructors)
'''class Employee:
    no_of_leaves = 10
    def __init__(self, names, new_salary, new_role):
        self.name = names
        self.salary = new_salary
        self.role = new_role

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"
Snehasis = Employee("Snehasis", 800000, "AI specialist and web developer")

print(Snehasis.printdetails())'''

# class method
'''class Employee:
    no_of_leaves = 10
    def __init__(self, names, new_salary, new_role):
        self.name = names
        self.salary = new_salary
        self.role = new_role

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves (cls, new_leaves):
        cls.no_of_leaves = new_leaves

Snehasis = Employee("Snehasis", 800000, "AI specialist and web developer")
Annesha = Employee("Annesha", 700000, "Software developer")

Snehasis.change_leaves(15)

print(Snehasis.printdetails())
print(Annesha.printdetails())

print(Snehasis.no_of_leaves)
print(Annesha.no_of_leaves)'''

# class method
'''class Employee:
    no_of_leaves = 10
    def __init__(self, names, new_salary, new_role):
        self.name = names
        self.salary = new_salary
        self.role = new_role

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves (cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)

Snehasis = Employee("Snehasis", 800000, "AI specialist and web developer")
Annesha = Employee("Annesha", 700000, "Software developer")
MondalRoy = Employee.from_str("MondalRoy-650000-Tech Support")
Snehasis.change_leaves(15)

print(Snehasis.printdetails())
print(Annesha.printdetails())
print(MondalRoy.printdetails())

print(Snehasis.no_of_leaves)
print(Annesha.no_of_leaves)'''

# Public, Private & Protected Access Specifiers
# Public -
# Protected -
# Private -
'''class Employee:
    no_of_leaves = 10
    var = 8
    _protec = 9
    __pr = 98
    def __init__(self, names, new_salary, new_role):
        self.name = names
        self.salary = new_salary
        self.role = new_role

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves (cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_str(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
    
    @staticmethod
    def printgood(string):
        print("This is good " + string)

Snehasis = Employee("Snehasis", 800000, "AI specialist and web developer")
Annesha = Employee("Annesha", 700000, "Software developer")
MondalRoy = Employee.from_str("MondalRoy-650000-Tech Support")
Snehasis.change_leaves(15)

print(Snehasis.printdetails())
print(Annesha.printdetails())
print(MondalRoy.printdetails())

print(Snehasis.no_of_leaves)
print(Annesha.no_of_leaves)
emp = Employee("Snehasis", 800000, "AI specialist and web developer")
print(emp._Employee__pr)'''

# Super() and Overriding In Classes
'''class A:
    classvar1 = "I am in class varible in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"  #as here is an instance varible then return will b printed this instance varible else it will return the prebious variable value
        self.special = "Special"

class B(A):
    classvar2 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class B"#as here is an instance varible then return will b printed this instance varible else it will return the prebious variable value

a = A()
b = B()

print(b.special)'''

# Operator Overloading & Dunder Methods
'''class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Snehasis", 800000, "AI specialist and web developer")
emp2 =Employee("Annesha", 700000, "Software developer")
print(str(emp1))'''

# from abc import ABCMeta, abstractmethod
'''from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle:
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 20
        self.breath = 10

    def printarea(self):
        return self.length * self.breath
rect1 = Rectangle()
print(rect1.printarea())'''

# Setters & Property Decorators 
'''class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)
hindustani_supporter.email = "this.that@codewithharry.com"
print(hindustani_supporter.fname)

del hindustani_supporter.email
print(hindustani_supporter.email)
hindustani_supporter.email = "Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)'''

# Generators In Python
'''def gen(n):
    for i in range(n):
        yield i
g = gen(3)
print(g)
# print(g.__next__())
# print(g.__next__())
# for i in g:
    # print(i)
s = "Snehasis"
ier = iter(s)
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
# print(ier.__next__())
for i in s:
    print(i)'''

# function chaching
'''import time
from functools import lru_cache
@lru_cache(maxsize=30)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(2)
    some_work(4)
    print("Done....Calling again")
    some_work(3)
    print("Called again")'''

# Else & Finally In Try Except
'''f1 = open("py.txt")

try:
    f = open("py.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")'''

# Coroutines In Python
'''def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")'''

# Pickle Module
# import pickle

# file pickling
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj) #object, fileobject
# fileobj.close()

# file depickling
'''file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))'''

# Raise In Python + Examples

# a = input("What is your name: ")
# b = input("How much do you earn: ")
# if int(b)==0:
    # raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
    # raise Exception("Numbers are not allowed")
# print(f"Hello {a}")
# 1000 lines taking 1 hour

'''c = input("Enter your name: ")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")'''

# Creating a Command Line Utility In Python 
'''import argparse
import sys
def calc(args):
    if args.o == 'add':
        return args.x + args.y
    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,help="Enter first number. This is a utility for calculation. Please contact")
    parser.add_argument('--y', type=float, default=3.0,help="Enter second number. This is a utility for calculation. Please contact")
    parser.add_argument('--o', type=str, default="add",help="This is a utility for calculation. Please contact for more")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))'''


