# A procedure, called biggest, which returns the key 
# corresponding to the entry with the largest number 
# of values associated with it. If there is more than 
# one such entry, return the first maching key.


def biggest(aDict):
    '''
    Args:
        aDict: A dictionary, where all the values are lists.

    Returns: 
        The key with the largest number of values associated with it.
    '''
    big = 0
    for key in aDict:
        if len(aDict[key]) > big:
            big = len(aDict[key])
            result = key
    return result

# Test case
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(biggest(animals))
