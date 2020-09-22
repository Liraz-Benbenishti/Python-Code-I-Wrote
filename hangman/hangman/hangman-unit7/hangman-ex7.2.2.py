def numbers_letters_count(my_str):
	"""
	The function gets as parameter a string.
	The function returns list where the first element is the number of digits in the string, and the second element is the number of characters in the string.
	:param my_str: The string to loop through.
	:type my_str: string
	:return: Returns a list where the first element is the number of digits in the string, and the second element is the number of characters in the string.
	rtype: list
	"""
	num_of_digits = 0
	num_of_non_digits = 0;
	for char in my_str:
		if ("0" <= char <= "9"):
			num_of_digits = num_of_digits + 1
		else:
			num_of_non_digits = num_of_non_digits + 1
	return [num_of_digits, num_of_non_digits]
	
def main():
	print(numbers_letters_count("Python 3.6.3"))
	
if __name__ == "__main__":
	main()