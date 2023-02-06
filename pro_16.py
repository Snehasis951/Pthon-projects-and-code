import bisect

list_1 = [1,2,5,10,15,17,28,35,59,61]
print(bisect.bisect(list_1, 25))
bisect.insort(list_1, 25)
print(list_1)

list_2 = ["a","f", "h", "l", "s", "y"]
print(bisect.bisect(list_2, "m"))
bisect.insort(list_2, "m")
print(list_2)

