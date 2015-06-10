start_number = 1000
for number in xrange(start_number, -1, -1):
	last_index = len(str(number)) - 1
	for number_index in xrange(0, last_index):
		num = str(number)
		if num[number_index] == num[last_index-number_index] and \
		number_index != last_index-number_index:
			print num
