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
	
def joes_solution(coins, value):
    """
    This takes in a list of coin denominations as coins i.e. [1, 4, 5, 9]
    and a value which is the change you want to give
    """
    table = [None for x in range(value + 1)] # creates a list with None as big as the change is i.e. if value = 4, table = [None, None, None, None, None] (0, 1, 2, 3, 4)
    table[0] = [] # initializes the first element in table to be an empty list
    for i in range(1, value + 1): # if value = 4 => [1, 2, 3, 4]
        for coin in coins: # for each of the coin values i.e. if coins =[1, 4, 5, 9], coin 1 then 4 then 5 then 9
            if coin > i: continue #if the coin denomination is bigger than i, just continue. 4 > 1, 2, 3 so it just continues.
            elif not table[i] or len(table[i - coin]) + 1 < len(table[i]): #table[i] => None usually.  so if you do not None => True or len(table[4-3]) + 1 = len(None) + 1 = 2< len(table[i]) = 2<1
                if table[i - coin] != None: # table[4 - 3] = table[0] = [] != None ==> true
                    table[i] = table[i - coin][:] # table [1] = table [1 - 1][:]
                    table[i].append(coin) # table[1].append(1)


    if table[-1] != None:
        print '%d coins: %s' % (len(table[-1]), table[-1])
    else:
        print 'No solution possible'
