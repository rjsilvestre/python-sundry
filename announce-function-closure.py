# Closure test file with starred expressions. The nested function stores a
# function passed as argument to the parent function, receives the funcion
# arguments as its own aruments on a starred expression, prints the stored
# function name and arguments and returns the execution of the function.
# Based on a example on geeksforgeeks website.


def announce_function(func):
    """A function that creates functions that print the function name and
    its arguments prior its execution.
    """

    def announcement(*args):
        """Prints function and arguments prior its execution."""
        print(f'Executing {func.__name__} function with args: {args}.')
        return func(*args)

    return announcement

# Test cases
announce_max = announce_function(max)
print(announce_max(1, 2, 3))

announce_sum = announce_function(sum)
print(announce_sum([1, 2, 3]))

args = (4, 5, 6)
print(announce_max(*args))    # Expands the tupple assigned to the args variable
