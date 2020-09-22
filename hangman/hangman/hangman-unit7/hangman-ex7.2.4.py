def seven_boom(end_number):
	"""
	:param end_number: the number to end the loop.
	:type end_param: int
	:return: list in range of 0 and end_number (including), where some numbers replaced by "BOOM".
	rtype: list
	"""
	list_of_numbers = []
	
	for number in range(end_number + 1):
		list_of_numbers.append(number)
		if (number % 7 == 0):
			list_of_numbers[number] = 'BOOM'
		if (str(7) in str(number)):
			list_of_numbers[number] = 'BOOM'

	return list_of_numbers

def main():
	print(seven_boom(17))
	
if __name__ == "__main__":
	main()