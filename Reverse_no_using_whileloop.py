# WAP to reverse a number inputnum = 123      ExpectedOutput = 321

n = int(input("Enter a number: "))
rev = 0
while(n>0):
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10
print("The reverse is", rev)