# A program that prints the longest substring of s in which the letters occur 
# in alphabetical order. 
# This version goes through a string containing the alphabet for each element
# of the string to be searched and appends the current element to another list
# if it is found on a subsequent position on the alphabet. Compares if the  
# resulting list is the longest and returns it.


def sort_alphabet(s):
    '''
    Finds the longest alphebetized sub string on a string.

    Arg:
        s: the string to be searched.

    Returns:
        The longest alphebetized string or an empty string
        if none is found.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    j = 0
    sort = ''
    cur_sort = ''
    while i < len(s):
        while j < len(alphabet):
            if s[i] == alphabet[j]:
                cur_sort += s[i]
                if len(cur_sort) > len(sort):
                    sort = cur_sort
                break
            j += 1
        if j == len(alphabet):
            j = 0
            cur_sort = ''
        else:
            i += 1
    return sort

# Test case
string = 'azcbobobegghakl'
print(sort_alphabet(string))
