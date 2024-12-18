# Python program to interchange first and last elements in the list

my_list = [43, 78, 56, 87]
print(my_list)

# Interchange first and last value of the list

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print("The interchange values are: ", my_list)