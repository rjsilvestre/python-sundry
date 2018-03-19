def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """

    best_sum = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)+1):
            if sum(L[i:j]) > best_sum:
                best_sum = sum(L[i:j])
    return best_sum

# Test cases
print(max_contig_sum([3, 4, -1, 5, -4]))    # Prints 11
print(max_contig_sum([3, 4, -8, 15, -1, 2]))    # Prints 16
