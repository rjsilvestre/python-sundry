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
