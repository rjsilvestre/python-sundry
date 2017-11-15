def genPrimes():
    '''
    a generator that returns the sequence of prime numbers
    on successive calls to its next() method.
    
    Yeilds:
        int: The next prime number
    '''
    prime = True
    primes = []
    x = 2
    while True:
        for p in primes:
            if not (x % p):
                prime = False
                break
        if prime == False:
            prime = True
        else:
            primes.append(x)
            yield x
        x += 1

#Test case
prime = genPrimes()
print(next(prime))
print(next(prime))
print(next(prime))
# or
print(prime.__next__())
print(prime.__next__())
print(prime.__next__())
