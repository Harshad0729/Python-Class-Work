# Q.2) Find Cube root of even numbers.

cubes = []
for x in range(11):
    if x % 2 == 0:
        cubes.append(x ** 3)
print("Listing for loops", cubes)


# Using list comprehension 
easy = [x ** 3 for x in range(11) if x % 2 == 0]
print("Using list comprehension", easy)