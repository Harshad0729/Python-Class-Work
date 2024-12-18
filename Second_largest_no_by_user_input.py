# Taking user input for the list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by commas: ").split(',')))

# Finding the maximum value
maximum_val = max(numbers)
print("The maximum value of the list is", maximum_val)

# Finding the minimum value
minimum_val = min(numbers)
print("The minimum value of the list is", minimum_val)

# Sorting the list in descending order to find the second largest number
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[i]:
            # Swap elements if the next element is greater
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

print("Sorted list:", numbers)
print("The second largest value is", numbers[1])