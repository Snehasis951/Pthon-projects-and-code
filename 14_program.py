# Python Program to Count the Number of Digits in a Number
n = int(input("enter a number: "))
count = 0
while (n>0):
    count= count+1
    n = n//10 
    # n = n//10 
    # this has focused on number of interation, 
    # the nuumber will be divided through each iteration and 
    # increment will be done by 1 number
print("the number of digit in given number: ", count)
