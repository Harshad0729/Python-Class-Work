num = int(input("Enter a positive number: "))
factorial = 1
original_num = num

while num > 1:
    factorial *= num
    num -= 1
    
print(f"The factorial of {original_num} is: {factorial}")

'''
5! = 5 * 4 * 3 * 2 * 1 = 120

iteration 1: num = 5        5 > 1 T
    factorial = factorial * num = 1 * 5 = 5
    num = 5 - 1 = 4
    
iteration 2: num = 4        4 > 1 T
    factorial = factorial * num = 5 * 4 = 20
    num = 4 - 1 = 3
    
iteration 3: num = 3        3 > 1 T
    factorial = factorial * num = 20 * 3 = 60
    num = 3 - 1 = 2
'''