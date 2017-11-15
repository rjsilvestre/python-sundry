def general_poly(L):
    """ 
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
    if isinstance(L, list):
        global polys
        polys = L
        return general_poly
    else:
        res = 0
        k = len(polys) - 1
        for n in polys:
            res += n * L**k
            k -= 1
        return res

# Test case
print(general_poly([1,2,3,4])(10))
