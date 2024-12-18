'''
Ordered:
When we say that tuples are orderd, it means that the items have a defined order, and
that order will not change.

Unchangeable: 
Tuples are unchangeable, meaning that we cannot change, add or remove 
items after the tuple has been created.

Allow Duplicates:
Since tuples are indexed, they can have items with the same value:
'''
thistuple = ("Apple", "Banana", "Cherry", "Apple","Cherry")
print(thistuple)

# Find the length of the tuple
print(len(thistuple))

# Tuple is also recognized by its index number
print(thistuple[0])
print(thistuple[3])

print(thistuple[2:4])