import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    same_color = 0
    for trial in range(numTrials):
        bucket = ['g', 'r'] * 4
        random.shuffle(bucket)
        drawn = []
        for i in range(3):
            drawn.append(bucket.pop())
        if len(set(drawn)) == 1:
            same_color += 1
    return same_color/numTrials


# Test cases
print(drawing_without_replacement_sim(100))
print(drawing_without_replacement_sim(1000))
print(drawing_without_replacement_sim(10000))
print(drawing_without_replacement_sim(1000000))
print(drawing_without_replacement_sim(1000000))
print(drawing_without_replacement_sim(1000000))
