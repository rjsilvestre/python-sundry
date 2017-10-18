# We can use the idea of bisection search to determine if a character is in a string, 
# so long as the string is sorted in alphabetical order.
# First, test the middle character of a string against the character you're looking for.
# If they are the same, we are done - we've found the character we're looking for!
# If they're not the same, check if the test character is "smaller" than the middle character.
# If so, we need only consider the lower half of the string; otherwise,
# we only consider the upper half of the string.


def isIn(char, aStr):
    '''
    Checks if a character is in an alpabetized string

    Args:
        char: a single character
        aStr: an alphabetized string

    Return: 
        True if char is in aStr; False otherwise
    '''
    mid_i = len(aStr) // 2
    if aStr == '':
        return False
    elif len(aStr) == 1:
        if aStr == char:
            return True
        return False
    else:
        if char == aStr[mid_i]:
            return True
        elif char > aStr[mid_i]:
            return isIn(char, aStr[mid_i + 1:])
        else:
            return isIn(char, aStr[:mid_i])
                
# Test case
aStr = 'abcdefhijklmnopqrstuvwxyz'
char = 'g'
print(isIn(char, aStr))
