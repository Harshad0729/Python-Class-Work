# List is a collection which is ordered and changeable.
# Allows duplicate members.

mylist = ["Oil","Soap",123,"Oil"]
print(mylist)
print(type(mylist))
print(mylist[0])

# Slicing list elements
print(mylist[1:])
print(mylist[2:5])

# You can use negative index as well
print(mylist[-1])
print(mylist[-2])

# Using for loop
for i in mylist:
    print(i)