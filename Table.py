# Ask the user for a number
number = int(input("Enter a number: "))  # Accept user input

# Print the multiplication table
for i in range(1, 11):  # Loop from 1 to 10
    print(number,"x", i, "=", number * i)  # Print the result using the specified format
