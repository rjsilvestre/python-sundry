def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''

    values = list(aDict.values())
    unique_keys = []
    for key in aDict:
        if values.count(aDict[key]) == 1:
            unique_keys.append(key)

    return sorted(unique_keys)

# Teste case
aDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 2}
print(uniqueValues(aDict))
