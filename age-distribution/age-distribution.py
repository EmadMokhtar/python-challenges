def detect_age(age):
	if age >= 0 and age <=2:
		return "Still in Mama's arms"
	elif age >= 3 and age <=4:
		return "Preschool Maniac"
	elif age >= 5 and age <=11:
		return "Elementary school"
	elif age >= 12 and age <=14:
		return "Middle school"
	elif age >= 15 and age <=18:
		return "High school"
	elif age >= 19 and age <=22:
		return "College"
	elif age >= 23 and age <=65:
		return "Working for the man"
	elif age >= 66 and age <=100:
		return "The Golden Years"
	else:
		return "This program is for humans"

with open('test_file.txt','r') as test_file:
	for line in test_file:
		age = int(line.strip())
		print detect_age(age)

