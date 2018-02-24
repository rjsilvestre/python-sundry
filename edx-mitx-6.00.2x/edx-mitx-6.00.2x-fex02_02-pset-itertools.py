# Rewrite of the powerSet(items) generator from the first finger exercise
# problem to make use of these itertools module.
# Perform a test run. The runtime may not be noticeably different, but shorter,
# more elegant code is often a good investment, particularly if other
# programmers will be responsible for its upkeep in the future.
# The function names were changed to follow PEP8.

import itertools
import random
import time

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

def power_set(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo
# End of classes and functions provided by the course

# Power set generated with itertools module functions
# The purpose of the assignement is to be able to research and find solutions
# prior to trying to solve a problem from the start. After some websearches
# stack overflow, forum and other results the choosen solution is based on the
# python documentation itself:
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def fast_power_set(items):
    '''Generates a power set of a list of items.

    Args:
        items: list, items to generate the power set.

    Returns:
        Iterable, with all the combinations inside tuples.
    '''
    return itertools.chain.from_iterable(itertools.combinations(items, comb_len)
            for comb_len in range(len(items)+1))

# Test Case
# Creation of 5 random items
items = build_random_items(5)
# Time test with the original power set function
time_start = time.time()
for combo in power_set(items):
    print(combo)
print(time.time() - time_start, 'seconds')
time_start = time.time()
# Time test with the power set function using itertools
for combo in fast_power_set(items):
    print(combo)
print(time.time() - time_start, 'seconds')
