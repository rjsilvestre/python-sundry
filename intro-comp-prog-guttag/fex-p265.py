import matplotlib.pyplot as pl
from math import factorial

def binom_coef(n, k):
    """Calculates a binomial coefficient.
    This function is also present on the scipy.special module as binom.

    Args:
        n: int, number of trials
        k: int, number of successes

    Returns:
        float, the calculated binomial coefficient
    """
    return int(factorial(n) / (factorial(k) * factorial(n-k)))

def binom_prob(n, k, p_success):
    """Calculates binomial probability

    Args:
        n: int, number of trials
        k: int, number of successes
        p_success: float, the probability of success of a single trial

    Returns:
        float, the probability of k successes in n trials
    """
    return binom_coef(n, k) * p_success**k * (1-p_success)**(n-k)

def plot_binoms(min_n, max_n, k, p_success):
    """Plots the probability of a binomial distribuition from min_n to max_n
    trials with k successes.

    Args:
        min_n: int, minimun number of trials
        max_n: int, maximum number of trials
        k: int, number of successes
        p_success: float, probability of success of a single trial
    """
    probs = [binom_prob(n, k, p_success) for n in range(min_n, max_n + 1)]
    trials = list(range(min_n, max_n + 1))
    pl.title("Probability of getting two 3's")
    pl.xlabel("Number of trials")
    pl.ylabel("Probability of success")
    pl.plot(trials, probs)
    pl.show()

# Test case
print(plot_binoms(2, 100, 2, 1/6))
