def calculate_experince(experinces):
	years, months = 0, 0 
	for exp in experinces:
		years += exp['years']
		months += exp['months']

	years += months / 12
	months = months % 12

	print 'You have %s years and %s months experience'

with open('test_file.txt') as test_file:
	exp = {}
	years, months = 0, 0 
	for line in test_file:

		line_years, line_month = [int(item) for item in line.strip().split(",")]
		years += line_years
		months += line_month

	years += months / 12
	months = months % 12
	print 'You have %s years and %s months experience' % (years, months)

