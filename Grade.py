# WAP to accept percentage from user and make decision on Grade.
# if percentage greater than or equal to 75 marks as 'O grade'
# if percentage greater than or equal to 60 marks as 'A grade'
# if percentage greater than or equal to 50 marks as 'B grade'
# if percentage greater than or equal to 40 marks as 'c grade'
# Otherwise print as failed

marks = int(input("Enter Marks: "))
if(marks>=75):
    print("O Grade!!!")
elif(marks>=60):
    print("A Grade!!!")
elif(marks>=50):
    print("B Grade!!!")
elif(marks>=40):
    print("C Grade!!!")
else:
    print("Failed!!!")