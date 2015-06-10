import string
import collections

with open('test_file.txt', 'r') as test_file:
	for line in test_file:
		line = line.rstrip().lower()
		l = collections.Counter(line)
		beauty = 26
		score = 0
		for key, value in l.most_common():
			if key.isalpha():
				score += (value * beauty)
				beauty -= 1
		print score