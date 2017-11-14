# A program that prints the longest substring of s in which the letters occur 
# in alphabetical order. 
# This version goes through all elements and directly compares the current 
# character with the next. If the next is higher, appends it to another list.
# Compares if the resulting list is the longest and returns it.


def sort_alphabet(s):
    '''
    Finds the longest alphabetized sub string on a string.

    Arg:
        s: The string to be searched.

    Returns:
        The longest alphabetized string.
    '''
    sort = s[0]
    cur_sort = s[0]
    for i in range(len(s) - 1):
        if s[i + 1] >= s[i]: 
            cur_sort += s[i + 1]
            if len(cur_sort) > len(sort):
                sort = cur_sort
        else:
            cur_sort = s[i + 1]
    return sort

# Test case
string = 'azcbobobegghakl'
print(sort_alphabet(string))
