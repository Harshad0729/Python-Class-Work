# WAP to search particular element in list

fruits = ["apple", "banana", "cherry", "date"]
target = "banana"

for fruit in fruits:
    if fruit == target:
        print("Found it!", fruit)
        break
    else:
        print("Not found!")