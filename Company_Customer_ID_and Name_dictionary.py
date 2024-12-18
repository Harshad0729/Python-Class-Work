# Company Customer ID and Name dictionary

customers = {
    1001:"John Doe",
    1002:"Jane Smith",
    1003:"Emily Johnson"
}
print(customers)

# Accessing Elements
x = customers[1001]
print(x)

x = customers.get(1002)
print(x)

# Get all the keys from the dictionary
y = customers.keys()
print(y)

# Update the Name of a particular customer
customers.update({1001:"Johnathan Doe"})
print(customers)

# Adding items in the dictionary
customers[1004] = "Michael Brown"
print(customers)

customers[1005] = "Sarah Lee"
print(customers)

# Removing items in the dictionary using popitem
customers.popitem()
print(customers)

# Looping over dictionary keys
for i in customers:
    print(i)
    
# Looping over dictionary values by accessing each key
for i in customers:
    print(customers[i])
    
# Looping using Values() and Keys() methods
print("Use of Values() method")
for i in customers.values():
    print(i)
    
print("Use of Keys() method")
for i in customers.keys():
    print(i)
    
# Traversing Dictionary
for x, y in customers.items():
    print(x, y)