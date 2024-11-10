# Initialize an empty list to store the first 20 even numbers
even_numbers = []

# Calculate the first 20 even numbers
for i in range(20):
    even_numbers.append(i * 2)  # i * 2 gives the even number

# Print the even numbers in reverse order
for number in reversed(even_numbers):
    print(number)
