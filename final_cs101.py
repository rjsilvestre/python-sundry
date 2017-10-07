# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def get_next_user(string_input, pos):
    period_pos = string_input.find('.', pos)
    user_end_pos = string_input.find(' ', period_pos)
    return string_input[period_pos + 1:user_end_pos], user_end_pos
    
def get_all_users(string_input):
    users = []
    next_pos = 0
    string_input = '.' + string_input
    while get_next_user(string_input, next_pos)[1] != -1:
        user, next_pos = get_next_user(string_input, next_pos)
        next_pos += 1
        if user not in users:
            users.append(user)
            
    return users
    
def get_info(string_input, user, string_sufix):
    string_info = user + string_sufix
    start_pos = string_input.find(string_info) + len(string_info)
    end_pos = string_input.find('.', start_pos)
    return string_input[start_pos:end_pos].split(', ')
    
def create_data_structure(string_input):
    network = {}
    users = get_all_users(string_input)
    connections_string = ' is connected to '
    games_liked_string = ' likes to play '
    for user in users:
        network[user] = {}
        network[user]['connections'] = get_info(string_input, user, connections_string)
        network[user]['games liked'] = get_info(string_input, user, games_liked_string)
        
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
        return network[user]['connections']
    return None

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    if user in network:
        return network[user]['games liked']
    return None

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B not in network[user_A]['connections']:
            network[user_A]['connections'].append(user_B)
        return network
    return False

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user not in network:
        network[user] = {'connections': [], 'games liked': games}
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    secundary_connections = []
    if user in network:
        connections = network[user]['connections']
        for connection in connections:
            for secundary_connection in network[connection]['connections']:
                if secundary_connection not in secundary_connections:
                    secundary_connections.append(secundary_connection)
        return secundary_connections
	return None

# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    common_connections = 0
    if user_A in network and user_B in network:
        connections_a = network[user_A]['connections']
        connections_b = network[user_B]['connections']
        for connection_a in connections_a:
            if connection_a in connections_b:
                common_connections += 1
        return common_connections
    return False

# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def find_path_to_friend(network, user_A, user_B, checked = None):
    if checked is None:
        checked = []
    if user_A in network and user_B in network:
        checked.append(user_A)
        connections = network[user_A]['connections']
        if user_B in connections:
            return [user_A, user_B]
        else:
            for user in connections:
                if user not in checked:
                    path = find_path_to_friend(network, user, user_B, checked)
                    if path:
                        return [user_A] + path
	return None

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Recommend Connections
# ----------------------------------------------------------------------------- 
# This function uses previous created functions and new ones to recommend new
# connections for a user.
# The user and network are the only required parameters.
# For all the current connections grab all the secondary connections.
# From all the secundary connections count the common connections and the common games.
# Rank the connections by number of common games and common connections. Where the ranking
# is calculated by weighting the games in common by 60% and the friends in common by 40%.
# This weight take in consideration that this is a gamming social network and the games are
# the common denominator and motivation for the user to join in the community.
# Order the users by ranking and return a list with the results.
def filter_secondary_connections(network, user, secondary_connections):
    filtered_connections = []
    connections = network[user]['connections']
    for secundary_connection in secondary_connections:
        if secundary_connection != user and secundary_connection not in connections:
            filtered_connections.append(secundary_connection)
    return filtered_connections
	
def count_common_games(network, user_A, user_B):
    common_games = 0
    if user_A in network and user_B in network:
        games_a = network[user_A]['games liked']
        games_b = network[user_B]['games liked']
        for game_a in games_a:
            if game_a in games_b:
                common_games += 1
        return common_games
    return False

def quicksort_users(ranking, users):
    if not users or len(users) <= 1:
        return users
    else:
        pivot = ranking[users[0]]
        lesser = []
        greater = []
        for user in users[1:]:
            if ranking[user] > pivot:
                greater.append(user)
            else:
                lesser.append(user)
    return quicksort_users(ranking, greater) + [users[0]] + quicksort_users(ranking, lesser)

def recommend_connections(network, user):
    d = 0.6
    rankings = {}
    secondary_connections = filter_secondary_connections(network, user, get_secondary_connections(network, user))
    if secondary_connections:
        for secondary_connection in secondary_connections:
            connection_score = count_common_connections(network, user, secondary_connection)
            game_score = count_common_games(network, user, secondary_connection)
            aggregate_score = (connection_score * (1 - d) + game_score * d)
            rankings[secondary_connection] = aggregate_score
        return quicksort_users(rankings, secondary_connections)
    return None

#net = create_data_structure(example_input)
#print net
#print get_connections(net, "Debra")
#print get_connections(net, "Mercedes")
#print get_games_liked(net, "John")
#print add_connection(net, "John", "Freda")
#print add_new_user(net, "Debra", []) 
#print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
#print get_secondary_connections(net, "Mercedes")
#print count_common_connections(net, "Mercedes", "John")
#print find_path_to_friend(net, "John", "Ollie")
#print recommend_connections(net, "John")
