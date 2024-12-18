# A dictionary is a built-in data structure in python that allows you to store
# A collection of key-value pairs.

# Dictionary is mutable and it ia unordered

my_dict = {
    "Std_ID":101,
    "Std_Name":"Harshad",
    "Course":"BCA"
}
print(my_dict)


# Accessing Elements

x = my_dict["Course"]
print(x)

x = my_dict.get("Std_Name")
print(x)


# Get all the keys from specified dictionary
y = my_dict.keys()
print(y)


# To Update particular value 

my_dict.update({"Std_Name":"Me"})
print(my_dict)


# Addting items in the dictionary 

my_dict["Fees"] = 45000
print(my_dict)

my_dict["Std_Address"] = "Navi Mumbai"
print(my_dict)


# Removing items in the dictionary using pop

my_dict.popitem()
print(my_dict)


# Looping over dictionary 

for i in my_dict:
    print(i)
    

# Looping over items in list

for i in my_dict:
    print(my_dict[i])

# Looping by the method Values() and Keys()

print("Use of Values() method")  
for i in my_dict.values():
    print(i)
    
print("Use of Keys() method")
for i in my_dict.keys():
    print(i)
    

# Traversing Dictionary
for x,y in my_dict.items():
    print(x,y)