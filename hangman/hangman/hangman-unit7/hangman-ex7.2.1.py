def is_greater(my_list, n):
	""""
	The function gets two parameters: a list and int n.
	The function returns new list with all the number that greater than n.
	:param my_list: list of numbers.
	:param n: a number.
	:type my_list: list
	:type n: int
	:return: List of the numbers bigger than n.
	rtype: list
	"""
	new_list = []
	for element in my_list:
		if (element > n):
			new_list.append(element)
	
	return new_list
	
def main():
	result = is_greater([1, 30, 25, 60, 27, 28], 28)
	print(result)
	
if __name__ == "__main__":
	main()