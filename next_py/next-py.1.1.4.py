import functools

def count_digits(num1, num2):
	"""
	:param num1: gets a string that represent a number.
	:type number: string
	:param num2: gets a string that represent a number.
	:type number: string
	:return: returns the sum of the numbers.
	rtype: integer
	"""
	return int(num1) + int(num2)
	
def sum_of_digits(number):
	"""
	:param number: gets a number.
	:type number: integer
	:return: returns the sum of its digits.
	rtype: integer
	"""
	return functools.reduce(count_digits, list(str(number)))
	

def main():
	print(sum_of_digits(104))
	
	
if __name__ == "__main__":
	main()