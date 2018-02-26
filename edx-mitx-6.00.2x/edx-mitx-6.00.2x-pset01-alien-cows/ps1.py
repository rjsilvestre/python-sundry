###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10, remain=[]):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if not remain:
        remain = sorted(list(cows.keys()), key=cows.get, reverse=True)
    if sum(cows[cow] for cow in remain) <= limit:
        return [remain]
    trip = []
    limit_avail = limit
    for cow in remain[:]:
        if cows[cow] <= limit_avail:
            trip.append(cow)
            remain.remove(cow)
            limit_avail -= cows[cow]
    all_trips = greedy_cow_transport(cows, limit, remain)
    all_trips.append(trip)
    return all_trips


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_list = list(cows.keys())
    best_trips = None
    for all_trips in get_partitions(cows_list):
        valid_trips = True
        for trip in all_trips:
            if sum(cows[cow] for cow in trip) > limit:
                valid_trips = False
        if valid_trips and (not best_trips or len(all_trips) < len(best_trips)):
            best_trips = all_trips
    return best_trips

# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
cows2 = {'Miss Bella': 15, 'Louis': 45, 'Patches': 60, 'Polaris': 20, 'Horns': 50, 'Milkshake': 75, 'MooMoo': 85, 'Muscles': 65, 'Clover': 5, 'Lotus': 10}

limit=10
print(cows)
print(cows2)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

