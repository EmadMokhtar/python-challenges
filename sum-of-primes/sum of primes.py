from math import sqrt
from itertools import count, islice

def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n % number:
            return False
    return True

counter = 0
prime_sum = 0
number = 0
while counter < 1000:
	if isPrime(number):
		prime_sum += number
		counter += 1
	number += 1
print prime_sum