# Write a generator that returns every arragement of items such that is in one
# or none of two different bags. Each comination should be given as a tuple of
# two lists, the first being the items of bag 1 and the second being of items of
# bag 2.


import random

# Classes and functions provided by the course.
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def get_name(self):
        return self.name
    def get_value(self):
        return self.value
    def get_weight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def build_items():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def build_random_items(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]
# End of classes and functions provided by the course.

def yield_all_combos(items):
    ''' Generates all combinations of N items into two bags, whereby each
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list
    of which item(s) are in each bag.
    '''
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test jth position of a base3 number
            if (i // 3**j) % 3 == 1:
                combo1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                combo2.append(items[j])
        yield combo1, combo2

# Test Case
items = build_random_items(3)
for item in items:
    print(item)
for combo1, combo2 in yield_all_combos(items):
    print('Combo1:')
    for item in combo1:
        print(item)
    print('Combo2:')
    for item in combo2:
        print(item)
    print('-----')
