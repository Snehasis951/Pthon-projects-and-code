# Python Program to Print all Numbers in a Range Divisible by a Given Number
x = int(input("Enter lower range limit: "))
y = int(input("Enter upper range limit: "))
z = int(input("Enter the number to be divided by: "))
for i in range(x,y+1):
    if(i%z == 0):
        print(i)

