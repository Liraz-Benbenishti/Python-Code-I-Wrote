def squared_numbers(start, stop):
	"""
	The function get to integers.
	The function returns list with the squares of the numbers between start and stop.
	:param start: The number the loop start from.
	:param stop: The number the loop end.
	:type start: int
	:type stop: int
	:return: list with the squares of numbers between start and stop.
	rtype: list
	"""
	list_to_return = []
	while (start <= stop):
		list_to_return.append(start ** 2)
		start = start + 1
	return list_to_return
		
def main():
	print(squared_numbers(4, 8))
	print(squared_numbers(-3, 3))
	
if __name__ == "__main__":
	main()