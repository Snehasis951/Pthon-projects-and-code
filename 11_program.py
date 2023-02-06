# Python Program to Print Odd Numbers Within a Given Range
x = int(input("Enter lower range limit: "))
y = int(input("Enter upper range limit: "))
for i in range(x,y+1):
    if i%2 != 0:
        print(i)
