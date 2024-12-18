# Write a program to find addition and subtraction using inheritance concept

# Parent class
class MathOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

# Child class inheriting from MathOperations
class Calculator(MathOperations):
    def addition(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Creating an object of the Calculator class
calc = Calculator(num1, num2)

# Output the addition and subtraction
print(f"Addition: {calc.addition()}")
print(f"Subtraction: {calc.subtraction()}")
