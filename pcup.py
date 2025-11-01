def calculate_rectangle_perimeter(length, width):
    """Calculates the perimeter of a rectangle."""
    return 2 * (length + width)

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = calculate_rectangle_perimeter(length, width)
print(f"The perimeter of the rectangle is: {perimeter}")
2. Perimeter of a Square:
Python

def calculate_square_perimeter(side):
    """Calculates the perimeter of a square."""
    return 4 * side

# Example usage:
side = float(input("Enter the side length of the square: "))
perimeter = calculate_square_perimeter(side)
print(f"The perimeter of the square is: {perimeter}")
3. Perimeter of a Circle (Circumference):
Python

import math

def calculate_circle_perimeter(radius):
    """Calculates the circumference (perimeter) of a circle."""
    return 2 * math.pi * radius

# Example usage:
radius = float(input("Enter the radius of the circle: "))
perimeter = calculate_circle_perimeter(radius)
print(f"The circumference of the circle is: {perimeter}")
4. Perimeter of a Triangle:
Python

def calculate_triangle_perimeter(side1, side2, side3):
    """Calculates the perimeter of a triangle."""
    return side1 + side2 + side3

# Example usage:
side1 = float(input("Enter the length of side 1 of the triangle: "))
side2 = float(input("Enter the length of side 2 of the triangle: "))
side3 = float(input("Enter the length of side 3 of the triangle: "))
perimeter = calculate_triangle_perimeter(side1, side2, side3)
print(f"The perimeter of the triangle is: {perimeter}")