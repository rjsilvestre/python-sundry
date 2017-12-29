# Implementation of an iterable object. Based on programiz.com example.
# Creates two instances of the objects PowerTwo with argument n, that when
# iterated prints the first n+1 power of two numbers.

class PowerTwo:
    """Iterates to the first n power of two numbers."""
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.next = 0
        return self

    def __next__(self):
        if self.next < self.n:
            result = 2 ** self.next
            self.next += 1
            return result
        else:
            raise StopIteration

# Test case
a = PowerTwo(4)
b = PowerTwo(10)

print()
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
