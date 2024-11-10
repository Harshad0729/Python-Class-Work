# WAP to check whether the number is palindrome or not.
n = int(input("Enter a number: "))
temp = n 
rev = 0
while(n>0):
    rem = n % 0
    rev = rev * 10 + rem
    n = n // 10
print("The reverse is", rev)
if(temp==rev):
    print("The numbe is palindrome number", temp)
else:
    print("The numbe is not palindrome number")