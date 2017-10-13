def sort_alphabet(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 0
    j = 0
    sort = ''
    cur_sort = ''
    while i < len(s):
        while j < len(alphabet):
            if s[i] == alphabet[j]:
                cur_sort += s[i]
                if len(cur_sort) > len(sort):
                    sort = cur_sort
                break
            j += 1
        if j == len(alphabet):
            j = 0
            cur_sort = ''
        else:
            i += 1
    return sort

# Test case
string = 'azcbobobegghakl'
print(sort_alphabet(string))
