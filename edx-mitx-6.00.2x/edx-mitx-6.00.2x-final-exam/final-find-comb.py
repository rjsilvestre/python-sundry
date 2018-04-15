import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    best_comb = None
    num_choices = None
    for i in range(2 ** len(choices)):
        result = 0
        comb = list(map(int, bin(i)[2:].zfill(len(choices))))
        for i in range(len(choices)):
            result += choices[i] * comb[i]
        if result == total:
            if not num_choices or comb.count(1) < num_choices:
                best_comb = comb
                num_choices = comb.count(1)
    if best_comb:
        return np.array(best_comb)
    return find_combination(choices, total-1)


# Test cases

print(find_combination([1,2,2,3], 4))
print(find_combination([1,1,3,5,3], 5))
print(find_combination([1,1,3,5,3], 0))
print(find_combination([1,1,1,9], 4))
print(find_combination([4, 6, 3, 5, 2], 10))
