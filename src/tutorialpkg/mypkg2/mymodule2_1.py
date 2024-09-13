import math


def calculate_area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.

    Raises:
    ValueError: If the radius is negative.

    """

    if radius < 0:
        raise ValueError("The radius cannot be negative.")

    area = math.pi * (radius ** 2)
    return area
