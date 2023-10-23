'''
NAME:KELVIN NZIOKA
REG_NO: PA106/G/9983/20
'''


import math

# Function to compute the area of a rectangle
def area_rectangle(length, width):
    return length * width

# Function to compute the area of a circle
def area_circle(radius):
    return math.pi * (radius ** 2)

# Function to compute the area of a right-angled triangle
def area_triangle(base, height):
    return 0.5 * base * height

# Display the menu
print("Select a shape to compute the area:")
print("1. Rectangle")
print("2. Circle")
print("3. Right-Angled Triangle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = area_rectangle(length, width)
    print(f"Type of figure: Rectangle, Dimensions: Length = {length}, Width = {width}, Area = {area}")
elif choice == "2":
    radius = float(input("Enter the radius of the circle: "))
    area = area_circle(radius)
    print(f"Type of figure: Circle, Dimensions: Radius = {radius}, Area = {area}")
elif choice == "3":
    base = float(input("Enter the base of the right-angled triangle: "))
    height = float(input("Enter the height of the right-angled triangle: "))
    area = area_triangle(base, height)
    print(f"Type of figure: Right-Angled Triangle, Dimensions: Base = {base}, Height = {height}, Area = {area}")
else:
    print("Invalid choice. Please select 1, 2, or 3 for the corresponding figure.")

# Note: This program does not include error handling for invalid inputs (e.g., non-numeric inputs).
