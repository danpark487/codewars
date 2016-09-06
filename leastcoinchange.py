def coin_change(cash):
	"""
	Given cash, return least number of coins necessary 
	Using coin denominations of 1,4,5,9
	"""
	final_count = [0,0,0,0]
	amt_left = cash
	while amt_left > 0:
		if int(amt_left/9) > 0:
			final_count[3] += int(amt_left/9)
			amt_left -= 9 * int(amt_left/9)
		elif int(amt_left/5) > 0:
			final_count[2] += int(amt_left/5)
			amt_left -= 5 * int(amt_left/5)
		elif int(amt_left/4) > 0:
			final_count[1] += int(amt_left/4)
			amt_left -= 4 * int(amt_left/4)
		else: 
			final_count[0] += 1
			amt_left -= 1
	return final_count, sum(final_count)