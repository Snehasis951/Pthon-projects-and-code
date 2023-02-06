# Python Program to Find the Sum of Digits in a Number
x = int(input("enter a number: "))
sum = 0
while(x>0):
    p = x%10
    sum = sum+ p
    x =  x//10
print("the total sum of given number: ", sum)
