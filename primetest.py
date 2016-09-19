def prime_test(m,n):
	"""
	Compile list of prime numbers between m and n
	"""
	for num in range(m,n+1):
		counter = 2
		while counter < num:
			if num%counter == 0 and num != counter:
				break
			else:
				counter += 1
		else:
			prime_list.append(num)