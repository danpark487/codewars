# Description:

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

# For example:

# [2, 4, 0, 100, 4, 11, 2602, 36]

# Should return: 11

# [160, 3, 1719, 19, 11, 13, -21]

# Should return: 160

def find_outlier(integers):
	"""
	Takes in array of integers, returns the single integer that is different in divisibility (odd/even) from all other integers in list
	"""
    test_list = []
    for i in range(3): # checks if majority of integers are even/odd
        if integers[i]%2 == 0:
            test_list.append(i)
    if len(test_list) > 1: 
        return [num for num in integers if num%2 != 0][0]
    else: 
        return [num for num in integers if num%2 == 0][0]