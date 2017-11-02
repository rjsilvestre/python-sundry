# Fibonacci numbers. Calculates the nth Fibonacci number.
# This function uses recursive calls to calculate the value.


def fibo(n):
    '''
    Calculates the nth Fibonacci number recursevely.

    Args:
        n: Fibonacci number to be calculated

    Return:
        Nth Fibonacci number.
    '''
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

# Test Case
print(fibo(10))
