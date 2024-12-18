# Write a program to accept two numbers from the user and find area of rectangle and area of triangle

# Parent class
class Shape:
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def area(self):
        return self.dimension1 * self.dimension2

# Triangle class inheriting from Shape
class Triangle(Shape):
    def area(self):
        return 0.5 * self.dimension1 * self.dimension2

# Taking input for rectangle and triangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Creating objects
rectangle = Rectangle(length, width)
triangle = Triangle(base, height)

# Printing the areas
print(f"Area of rectangle: {rectangle.area()}")
print(f"Area of triangle: {triangle.area()}")
