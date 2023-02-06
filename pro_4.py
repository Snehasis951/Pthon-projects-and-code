# Map function 
def square(n):
    return n**2
h1 = [1,2,4,9,7]
# sq = []

# for item in h1:
    # sq.append(item**2)
sq = list(map(square, h1))
print(sq)

