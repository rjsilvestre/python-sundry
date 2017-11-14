def is_triangular(k):
    tri = 0
    for i in range(k + 1):
        tri += i
        if tri == k:
            return True
    return False

# Test case
print(is_triangular(1))
print(is_triangular(3))
print(is_triangular(6))
print(is_triangular(10))
print(is_triangular(4))
