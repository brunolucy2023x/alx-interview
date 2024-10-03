#scal_triangle
Author: Bruno Okoth
"""

def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal Triangle of height n.
    Returns an empty list if n <= 0.
    """
    k = []  # Initialize an empty list to hold the rows of Pascal's Triangle

    # Check if the input height n is less than or equal to 0
    if n <= 0:
        return k  # Return the empty list if n is not positive

    k = [[1]]  # The first row of Pascal's Triangle is always [1]

    # Loop through each row from 1 to n-1
    for i in range(1, n):
        temp = [1]  # Start each row with a 1
        # Loop through the previous row to calculate the values in the current row
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]  # Get the previous row
            # Calculate the value as the sum of two values from the previous row
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)  # End each row with a 1
        k.append(temp)  # Add the current row to the triangle

    return k  # Return the complete Pascal's Triangle
!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr = k[i - 1]
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
