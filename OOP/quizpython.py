import math

def calculate_triangle_height(side_length):
    """Calculate the height of an equilateral triangle given its side length."""
    return (math.sqrt(3) / 2) * side_length

def calculate_square_side_length(side_length):
    """
    Calculate the side length of a square inscribed in an equilateral triangle
    where one side of the square lies along the triangle's base.
    """
    return (side_length * (math.sqrt(3) - 1)) / (math.sqrt(3) + 1)

def calculate_square_area(square_side):
    """Calculate the area of a square given its side length."""
    return square_side ** 2

def area_of_inscribed_square(side_length):
    """Calculate and print the area of a square inscribed in an equilateral triangle."""
    # Step 1: Calculate the height of the triangle (not directly used but for reference)
    triangle_height = calculate_triangle_height(side_length)
    print(f"Height of the triangle: {triangle_height}")

    # Step 2: Calculate the side length of the inscribed square
    square_side = calculate_square_side_length(side_length)
    print(f"Side length of the inscribed square: {square_side}")

    # Step 3: Calculate the area of the inscribed square
    area_square = calculate_square_area(square_side)
    print(f"The area of the inscribed square is: {area_square}")

# Example usage with side length of 3
area_of_inscribed_square(3)

