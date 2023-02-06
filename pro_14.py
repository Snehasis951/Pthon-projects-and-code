# filter function 

def greater_than_2(n):
    if n>2:
        return True
    else:
        return False
    
h1 = [1,4,5,8,2,-8,-9]
greater_tha_2 = list(filter(greater_than_2, h1))
print(greater_tha_2)
