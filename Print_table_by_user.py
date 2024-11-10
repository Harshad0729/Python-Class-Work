# Get the number from the user
number = int(input("Enter the number for which you want to print the multiplication table: "))

# Print the multiplication table
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
