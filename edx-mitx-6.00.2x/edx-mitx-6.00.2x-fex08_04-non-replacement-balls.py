import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    valid = 0
    for t in range(numTrials):
        bucket = ['r', 'g'] * 3
        drawn = no_replacement_draw(bucket, 3)
        if drawn[1:] == drawn[:-1]:
            valid += 1
    return valid/numTrials

def no_replacement_draw(bucket, num_draws):
    '''
    Draws num_draws balls from bucket without replacement.
    Returns drawn balls list.
    '''
    draws = []
    for d in range(num_draws):
        draws.append(bucket.pop(random.randrange(len(bucket))))
    return draws

# Test cases
print(noReplacementSimulation(100000))
print(noReplacementSimulation(1000000))
print(noReplacementSimulation(10000000))
