#faulty calculator
'''design a calculator which will corrrectlysolve all the problem except the following ones: 45*3 = 555, 56+9 = 77, 56/6 = 4
your program shoul take operator and the two number as input from user and the return the result''' 
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 =input("What is your choice? " + "+,-,/,%,*: ")

if num1 == 45 and num2 == 3 and num3 =='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3 =='*' :
    num4 = num1 * num2
    print(num4)
elif num3 == '+':
    plus = num2 + num1
    print(plus)
elif num3 == '/':
    Dev = num2/num1
    print(Dev)
elif num3 == '-':
    Dev = num2-num1
    print(Dev)
elif num3 == '%':
    percent = num2%num1
    print(percent)
else:
    print("Error! Please check your input")
