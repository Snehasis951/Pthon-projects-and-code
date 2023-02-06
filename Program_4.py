# Health Management System
# 3 clients - Snehasis, Annesha and MondalRoy
'''def getdate():
    import datetime
    return datetime.datetime.now()'''
# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food: "))
        if(c==1):
            value=input("type here\n")
            with open("Snehasis-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("Snehasis-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("Annesha-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Annesha-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("MondalRoy-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("MondalRoy-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(Snehasis),2(Annesha),3(MondalRoy)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("Snehasis-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("Snehasis-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("Annesha-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Annesha-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("MondalRoy-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("MondalRoy-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (Snehasis, Annesha and MondalRoy)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for Snehasis  2 for Annesha and  3 for MondalRoy "))
    take(b)
else:
    b = int(input("Press 1 for Snehasis  2 for Annesha and  3 for MondalRoy"))
    retrieve(b)
  