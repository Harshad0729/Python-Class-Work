# WAP to find even number in the list

numbers = [34, 23, 12, 7, 91, 27]
even = []       # Empty list to store even numbers

for n in numbers:
    if n % 2 == 0:
        even.append(n)
print(even)