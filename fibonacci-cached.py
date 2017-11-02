# Fibonacci numbers. Calculates the nth Fibonacci number.
# This program uses a memoization technique to speed up 
# the function recursive calls.
# Also uses exception handling to capture python exceptions
# and return an error message to the user.


def cached_proc(f, arg, cache):
    '''
    Executes function f if the result is not already
    present in the dictionary cache. Returns f(arg).

    Args:
        f: A function.
        arg: An argument the function.
        cache: Dictionary with arguments and results pairs.

    Return:
        The result of the function f with the argument
        as parameter.
    '''
    if arg in cache:
        return cache[arg]
    else:
        result = f(arg)
        cache[arg] = result
        return result

def cached_fibo(n):
    '''
    Function is executed calling the helper function
    cached_proc to return cached values.

    Args:
        n: Fibonacci number to be calculated

    Return:
        Nth Fibonacci number.
    '''
    return (cached_proc(cached_fibo, n-1, fibo_cache) 
            + cached_proc(cached_fibo, n-2, fibo_cache))

try:
    fibo_cache = {0: 0, 1: 1}   # Initialization of the cache with base cases.
    n = int(input('Fibonacci number: '))
    print(cached_proc(cached_fibo, n, fibo_cache))   # Prints the nth Fibonacci number.
except RecursionError:
    print('The number is too big to be handled with recursion.')
except ValueError:
    print('Invalid number.')
