def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    cur_inc = [L[0]]
    cur_dec = [L[0]]
    best_inc = []
    best_dec = []
    for i in range(len(L) - 1):
        if L[i + 1] >= L[i]:
            cur_inc.append(L[i + 1])
            if len(cur_inc) > len(best_inc):
                best_inc = cur_inc[:]
        else:
            cur_inc = [L[i + 1]]

        if L[i + 1] <= L[i]:
            cur_dec.append(L[i + 1])
            if len(cur_dec) > len(best_dec):
                best_dec = cur_dec[:]
        else:
            cur_dec = [L[i + 1]]

        if len(best_inc) > len(best_dec):
            longest = best_inc
        elif len(best_inc) < len(best_dec):
            longest = best_dec
        elif best_inc == best_dec:
            longest = best_inc

    return sum(longest)

#Test case
L1 = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
L2 = [3, 3, 3, 3, 3]
L3 = [-3, -3, -3, -3, -3]
L4 = [5, 4, 10]
L5 = [3, 2, -1, 2, 7]
print(longest_run(L1))
print(longest_run(L2))
print(longest_run(L3))
print(longest_run(L4))
print(longest_run(L5))
