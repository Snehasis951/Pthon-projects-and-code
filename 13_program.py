# Python Program to Find the Smallest Divisor of an Integer
x = int(input("enter a number: "))
a =  []
for i in range(2, x+1):
    if(x%i == 0):
        a.append(i)
    a.sort()
print("smallest divisor is: ", a[0])
