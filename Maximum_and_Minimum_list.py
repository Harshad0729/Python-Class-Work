# WAP to get maximum and minimum of given list.

l = [45, 5, 67, 3, 24]
maximum_val = max(l)
print("The maximum value of list is", maximum_val)

minimum_val = min(l)
print("The minimum value of list is", minimum_val)

# Second largest

for i in range(0, 5):
    for j in range(i+1, 5):
        if l[j] > l[i]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)
print("Second largest", l[1])