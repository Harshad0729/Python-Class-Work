# Print multiplication tables for numbers from 2 to 6
for number in range(2, 7):  # Loop through numbers 2 to 6
    print(number)
    for i in range(1, 11):  # Loop from 1 to 10 for each number
        print(number,"x", i, "=", number * i)  # Print the result
    print()  # Print a newline for better readability between tables