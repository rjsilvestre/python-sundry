def sort_alphabet(s):
    sort = s[0]
    cur_sort = s[0]
    for i in range(len(s) - 1):
        if s[i + 1] >= s[i]: 
            cur_sort += s[i + 1]
            if len(cur_sort) > len(sort):
                sort = cur_sort
        else:
            cur_sort = s[i + 1]
    return sort

# Test case
print(sort_alphabet('azcbobobegghakl'))
