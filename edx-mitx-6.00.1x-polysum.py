# A regular polygon has 'n' number of sides. Each side has length 's'.
# The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
# The perimeter of a polygon is: length of the boundary of the polygon
# This function called 'polysum' that takes 2 arguments, 'n' and 's'.
# This function should sum the area and square of the perimeter of the 
# regular polygon. The function returns the sum, rounded to 4 decimal places.


import math

def polysum(n, s):
    '''
    Args:
        n: Number of sides of a polygon.
        s: Length of each side.

    Returns:
        The sum of the area and square of
        a polygon.
    '''
    area = (0.25*n*s**2) / math.tan(math.pi/n)
    perim = n*s
    result = round(area + perim**2, 4)
    return result

# Test case
print(polysum(70, 30))
