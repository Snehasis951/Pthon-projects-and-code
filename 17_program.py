# Python Program to Put Even and Odd elements in a List into Two Different Lists
def split(a):
    even_list =[]
    odd_list = []
    for b in a:
        if (b%2 == 0):
            even_list.append(b)
        else:
            odd_list.append(b)
    print("Even list is: ", even_list)
    print("Odd list is: ", odd_list)
a = [5,4,85,47,58,46,14,15,49,24,29]
split(a)







