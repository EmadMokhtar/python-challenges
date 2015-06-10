from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n % number:
            return False
    return True

def isPalindrome(n):
	last_index = len(str(n)) - 1
	if len(str(n)) < 2:
		return False
	for number_index in xrange(0, last_index):
		num = str(n)
		if num[number_index] != num[last_index-number_index] and \
		number_index != last_index-number_index:
			return False
		else:
			return True

start_number = 1000
for number in xrange(start_number, -1, -1):
	if isPrime(number) and isPalindrome(number):
		print number
		break