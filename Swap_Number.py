# Using input function take two number and then swap the number
 
# Taking input from the users 
a= int(input("Enter any number: "))
b = int(input("Enter any number: "))

# Before Swapping... 
print("Before Swapping")
print("A:",a)
print("B:",b)

# Using 'temp' variable for Swapping 
temp = a
a = b 
b = temp

# After Swapping...
print("After Swapping")
print("A:",a)
print("B:",b)