# Q.2) Write a program to find second largest number in a list.

l1 = [67,76,89,67,99,99]
print("The original list is", l1)
remove_dup = list(set(l1))
print("The final list is", remove_dup)
print(remove_dup)

sorted_list = sorted(remove_dup)
print(sorted_list)

print("The sorted elements in a list", sorted_list)

second_largest = sorted_list[-2]
print("The second largest number is:", second_largest)