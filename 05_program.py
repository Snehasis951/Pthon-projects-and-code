# Python Program to Reverse a Given Number
x=int(input("Enter a number: "))
rev = 0
while(x>0):
    p = x%10
    rev = rev*10 + p
    x = x//10
print("reverse of the number", rev)

