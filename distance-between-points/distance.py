from math import sqrt
from math import trunc

def distance_between_points(x1, y1, x2, y2):
	return int(sqrt((x1 - x2)**2 + (y1 - y2)**2))

with open('test_file.txt') as test_file:
	for line in test_file:
		line = line.replace('(', '').replace(')', '').replace(',', '')
		x1, y1, x2, y2 = [int(item) for item in line.split()]
		print distance_between_points(x1, y1, x2, y2)
