def isIn(char, aStr):
    '''
    char: a singe character
    aStr: an alphabetized string

    return: True if char is in aStr; False otherwise
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
