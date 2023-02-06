'''

iterable - which provide iterator 
iterator - object that helps to define next method
iteration - itrating any object and fetch it with next object is called iteration 

'''

def gen(n):
    for i in range(n):
        yield i

object1 = (gen(4))
# print(next(object1))
# print(next(object1))
# print(next(object1))
# print(next(object1))
# print(next(object1))
num1 = "Snehasis"
for i in num1:
    print(i)
