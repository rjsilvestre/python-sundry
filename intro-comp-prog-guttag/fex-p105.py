def find_an_even(l):
    """Assumes l is a list of integers.
    Returns the first even number in l.
    Raises ValueError if l does not contain an even number.
    """
    for e in l:
        if e%2 == 0:
            return e
    raise ValueError('Argument does not contain a even number.')

# Test cases
print(find_an_even([1,3,7,4,9,2]))
print(find_an_even([1,3,7,9]))   # Raises ValueError
