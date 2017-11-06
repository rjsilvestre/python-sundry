# Defined an intersect method that returns a new intSet containing 
# elements that appear in both sets.
# Added the appropriate method(s) so that len(s) returns the number
# of elements in s would return a new intSet of integers that appear
# in both s1 and s2.


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def __len__(self):
        """Return the lenght of self"""
        return len(self.vals)
    
    def intersect(self, other):
        """Returns a intSet object with the common values between
           self and other"""
        res = intSet()
        for e in self.vals:
            if other.member(e):
                res.insert(e)
        return res

# Test case
set_a = intSet()
set_b = intSet()

for e in range(5):
    set_a.insert(e)
for e in range(4, 9):
    set_b.insert(e)

print(len(set_a))
set_c = set_a.intersect(set_b)
print(set_c)
