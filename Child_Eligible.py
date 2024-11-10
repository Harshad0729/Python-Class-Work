# Accept age of child and make a decision whether he is eligible for play group, Nursury,Jr.kg, Sr.kg.


age = float(input("Enter the age of the Child: "))

if age < 3:
    print("Is Eligible for Play Group")
elif 3 <= age < 4:
    print("Is eligible for Nursery")
elif 4 <= age < 5:
    print("Is eligible for Junior KG")
elif age >= 5:
    print("Is eligible for Senior KG")
else:
    print("Invalid age entered")