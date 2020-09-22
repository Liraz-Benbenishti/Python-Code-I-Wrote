def distance(num1, num2, num3):
	if not ((abs(num2 - num1) == 1) or (abs(num3 - num1) == 1)):
		return False
	if (abs(num3 - num1) >= 2 and (abs(num3 - num2) >= 2)) or (abs(num2 - num1) >= 2 and (abs(num2 - num3) >= 2)):
		return True
	return False

print(distance(1, 2, 10))

print(distance(4, 5, 3))