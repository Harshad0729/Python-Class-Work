# WAP to swap two numbers in a list(list of 6) 2nd element with 4th element 

my_list = [1, 2, 3, 4, 5, 6]
print(my_list)

my_list[1], my_list[3] = my_list[3], my_list[1]
print("The interchanged values are:", my_list)