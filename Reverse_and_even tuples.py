# WAP to reverse the given tuple

tuple = (56, 78, 34, 89, 8)
print("The original tuple is:",tuple)
res = (tuple[::-1])
print("The reverse order is:")
print(res)

# WAP to print even numbers in tuple
for i in tuple:
    if i % 2 == 0:
        print(i)
        
tup2 = (45, [34,89], 80, 73, 45, 45, 90)
print(tup2[0])
print(tup2[1])
print(tup2[1][0])
print(tup2[1][1])

tup2[1][0] = 45
print(tup2)

# WAP to count the 45 in the tuple
print("The 45 occours ", tup2.count(45), "times")