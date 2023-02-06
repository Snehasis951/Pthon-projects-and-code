#Python Program to Merge Two Lists and Sort it
list1 = []
list2 = []
n1 = int(input("enter the number of elements: "))
n2 = int(input("enter the number of elements: "))
for i in range(1, n1+1):
    x = int(input("enter all the elements: "))
    list1.append(x)
for j in range(1, n2+1):
    y = int(input("enter all the elements: "))
    list2.append(y)
print("First list: ", list1)
print("Second list: ", list2)
list3 = list1 + list2
list3.sort()
print("Sorted list: ", list3)
