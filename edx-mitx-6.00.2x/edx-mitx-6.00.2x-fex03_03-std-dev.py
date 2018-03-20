# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and
# outputs the standard deviation of the lengths of the strings.
# Return float('NaN') if L is empty.

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """

    if not L:
        return float('NaN')

    mean = sum(len(e) for e in L) / len(L)
    total = 0.0
    for e in L:
        total += (len(e) - mean)**2
    std_dev = (total / len(L))**0.5
    return std_dev


# Test cases
L = ['a', 'z', 'p']
print(stdDevOfLengths(L))    # 0.0
L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))    # 1.8708
