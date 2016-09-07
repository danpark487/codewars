# Description:

# My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?
# Example:

# "56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

# When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9) it comes before as a string.

# All numbers in the list are positive numbers and the list can be empty.

def order_weight(strng):
	"""
	Take in string of numbers, add together the digits of those numbers
	Sort original string by the numerical order of the sum of its digits
	"""
	print(strng)
	strng_list = strng.split() # split input into list
	sum_digit_list = [] # empty string to compile sum of digits
	for i in strng_list:
		new_value = sum(int(x) for x in i) # find the sum of digits for each number in original string
		sum_digit_list.append(new_value)
	sorted_list = [x for (y,x) in sorted(zip(sum_digit_list, strng_list))] # sort the original list by the sorted digit_sum_list
	return " ".join(sorted_list)
	
def joes_version(numstring):
	num_list = numstring.split()
	sum_list = [(sum(int(x) for x in num_list[i]), i) for i in range(len(num_list))]
	ordered = {x:num_list[x] for x in range(len(num_list))}
	return [ordered[x[1]] for x in sorted(sum_list)]
