def mod(n, m):
	"""
	get the modulus of number m for n
	N MOD M
	"""
	division_result = n/m

	return n - (m * division_result)

with open('test_file.txt') as test_file:
	for line in test_file:
		n, m = [int(i) for i in line.strip().split(',')]

		print mod(n, m)
		print n % m