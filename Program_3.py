#pattern printing 
'''input = integer nonlocal
boolean = True or False
True n = 5
*
**
***
****
False n = 5
****
***
**
*'''

x = int(input("please add number of line you want to print: "))
y = bool(int(input("please add 0 for False: ")))


def star(x, y):
    if y == True:
        z = 1
        while z <= x:
            print(z * "*")
            z = z + 1
    else:
        while x > 0:
            print(x * "*")
            x = x - 1
star(x, y)