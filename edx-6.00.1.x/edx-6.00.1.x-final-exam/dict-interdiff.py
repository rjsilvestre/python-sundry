def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    inter = {}
    diff = {}
    for e in d1:
        if e in d2:
            inter[e] = f(d1[e], d2[e])
        else:
            diff[e] = d1[e]

    for e in d2:
        if e not in d1:
            diff[e] = d2[e]

    return (inter, diff)

#Test case
def f(a, b):
    return a > b
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}

#def f(a, b):
    #return a + b
#d1 = {1:30, 2:20, 3:30, 5:80}
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))
