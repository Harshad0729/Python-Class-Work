# Each product in a supermarket is associated with its price.

Products = {
    "Milk":1.5,
    "Bread":2.0,
    "Eggs":3.0
}
print(Products)


# Accessing Elements
x = Products["Bread"]
print(x)

x = Products.get("Milk")
print(x)


# Get all the keys the dictionary
y = Products.keys()
print(y)


# Update the price of particular product 
Products.update({"Milk":1.8})
print(Products)


# Adding items in the dictionary 
Products["Butter"] = 2.5
print(Products)

Products["Cheese"] = 3.5
print(Products)


# Removing items in the dictionary using popitem
Products.popitem()
print(Products)


# Looping over dictionary keys
for i in Products:
    print(i)
    

# Looping over dictionary values by accessing each keys
for i in Products:
    print(Products[i])
    

# Looping using values() and keys() methods
print("Use of Values() method")
for i in Products.values():
    print(i)
    
print("Use of keys() method")
for i in Products.keys():
    print(i)
    

# Traversing Dictionary 
for x, y in Products.items():
    print(x, y)