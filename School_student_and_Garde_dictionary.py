# Each students in a school is associated with their grade.

students = {
    "Alice":"A",
    "Bob":"B",
    "Charlie":"C"
}
print(students)


# Accessing Elements
x = students["Alice"]
print(x)

x = students.get("Bob")
print(x)


# Get all the keys from the dictionary
y = students.keys()
print(y)

# Update the grade of a particular student 
students.update({"Alice":"A+"})
print(students)

# Adding items in the dictionary
students["David"] = "A"
print(students)

students["Eve"] = "B+"
print(students)

# Removing items in the dictionary using popitem
students.popitem()
print(students)

# Looping over dictionary keys
for i in students:
    print(i)
    
# Looping over dictionary values by accessing each keys
for i in students:
    print(students[i])
    
# Looping using values() and keys() methods
print("Use of Values() method")
for i in students.values():
    print(i)
    
print("Use of Keys() method")
for i in students.keys():
    print(i)
    
# Traversing Dictionary
for x, y in students.items():
    print(x, y)