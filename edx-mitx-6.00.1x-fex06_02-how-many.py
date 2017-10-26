# A procedure, called how_many, which returns the sum of 
# the number of values associated with a dictionary. 


def how_many(aDict):
    '''
    Args:
        aDict: A dictionary, where all the values are lists.

    Returns: 
        int, how many values are in the dictionary.
    '''
    values = aDict.values()
    result = []
    for value in values:
        result.extend(value)
    return len(result)

# Test case
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
