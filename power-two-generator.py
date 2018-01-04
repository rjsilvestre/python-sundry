# Implementation of a generator object. Based on programiz.com example.
# Calls the function power_two with the argument max_n and prints the first
# max_n generated power of two numbers.

def power_two(max_n):
    """Generates the first max_n power of two numbers."""
    next_n = 0
    while next_n < max_n:
        yield 2 ** next_n
        next_n += 1

a = power_two(4)
for num in a:
    print(num)

# Prints nothing since the generator only iterates once
for num in a:
    print(num)

# Prints normaly since is an unassigned function
print()
for num in power_two(4):
    print(num)
