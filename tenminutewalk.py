# Description:

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

#     Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).

def isValidWalk(walk):
    """
    Checks whether a set of directions (n,s,e,w) where each takes 1 minute to walk
    will return to the same point in 10 minutes
    """
    print(walk) # prints directions input
    N = 0 # counters for directions
    S = 0
    E = 0
    W = 0
    total_min = 0 # check counter for total time elapsed in walk
    for directions in walk: # loop through directions 
        if directions == 'n':
            N += 1
            total_min += 1
        elif directions == 's':
            S -= 1
            total_min += 1
        elif directions == 'e':
            E += 1
            total_min += 1
        else:
            W -= 1
            total_min += 1
    if N + S + E + W != 0: # checks whether the directions bring back to starting point
        return False
    elif total_min != 10: # check whether total time of journey is longer than 10 minutes
        return False
    else:
        return True