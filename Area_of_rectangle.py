def calculate_area(length, width):
    return length * width

# Take user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_area(length, width)
print("The area of the rectangle is:", area)
