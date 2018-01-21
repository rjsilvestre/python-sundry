def sum_digits(s):
    """Assumes s is a string.
    Returns the sum of the secimal digis in s.
    For example , if s is 'a2b3c' it returns 5.
    """
    result = 0
    for e in s:
        try:
            result += int(e)
        except ValueError:
            pass
    return result

print(sum_digits('a2b3c'))
