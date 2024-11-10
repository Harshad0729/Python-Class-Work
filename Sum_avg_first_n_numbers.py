# Input: Get the number of natural numbers from the user
n = int(input("Enter the number of natural numbers you want to sum and average: "))

# Initialize sum
sum_of_natural_numbers = 0

# Calculate the sum of the first n natural numbers using a loop
for i in range(1, n + 1):
    sum_of_natural_numbers += i  # Add each number to the sum

# Calculate the average
average_of_natural_numbers = sum_of_natural_numbers / n  # Average is sum divided by n

# Output: Print the results
print("Sum of the first", n, "natural numbers is:", sum_of_natural_numbers)
print("Average of the first", n, "natural numbers is:", average_of_natural_numbers)
