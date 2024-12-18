# Q.3) Write a program to check whether the list is palindrome or not.


l = [45, 99, 23, 11, 23, 99, 45]
is_palindrome = l == l[::-1]

if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
