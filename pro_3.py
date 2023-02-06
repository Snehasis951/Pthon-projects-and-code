# *args and **kwargs 
# *vars and **kvars 

from ast import arg


def func_1(*args):
    # print(type(args))
    if (len(args)== 3):
        print("The name of the student is ", args[0], "and age is ", args[1], "and rollno is ", args[2])
    else:
        print("The name of the student is ", args[0], "and age is ", args[1])  

# func_1(*lis_1)

def print_marks(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

def master_class(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i)
    for key, value in kwargs.items():
        print(key, value)

lis_1 = ["Snehasis", 23]  

marks_list = {"Rijvan Ansari": 78, "Sandipan Sarkar": 84, "farhad khan": 81, "Snehasis Mondal": 99}
# print_marks(**marks_list)

master_class("normal_agrs", *lis_1, **marks_list)

