# Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = a + b 
b = c - b
a = c - b 
print("a is", a, "b is", b)
