# Python Program to Calculate the Average of Numbers in a Given List
n = int(input("enter the number of elements to be inserted: "))
a = []
for i in range (0,n):
    element = int(input("enter the element: "))
    a.append(element)
avg = sum(a)/ n
print("average of elements in the list", round(avg,3))

eval()