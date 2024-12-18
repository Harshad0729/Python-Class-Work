# Q.4) Write a program to do intersection of two list.

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example 
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print(intersection(lst1, lst2))