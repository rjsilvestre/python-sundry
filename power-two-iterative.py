# Implementation of an iterable object. Based on programiz.com example.
# Creates three instances of the objects PowerTwo with argument max_n, that when
# iterated prints the first max_n power of two numbers.

class PowerTwo:
    """Iterates through the first max_n power of two numbers."""
    def __init__(self, max_n):
        self.max_n = max_n

    def __iter__(self):
        self.next_n = 0
        return self

    def __next__(self):
        if self.next_n < self.max_n:
            result = 2 ** self.next_n
            self.next_n += 1
            return result
        else:
            raise StopIteration

# Test cases
a = PowerTwo(4)
b = PowerTwo(10)

for num in a:
    print(num)

print()
for num in b:
    print(num)

print()
for num in a:
    print(num)

c = iter(PowerTwo(3))
print()
print(next(c))
print(next(c))

c = iter(c)   # Reset the iteration of c
print()
print(next(c))
print(next(c))
print(next(c))
print(next(c))   # Will raise StopIteration error
