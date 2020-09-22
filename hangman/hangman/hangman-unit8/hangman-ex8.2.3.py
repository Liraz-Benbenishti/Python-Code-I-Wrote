def mult_tuple(tuple1, tuple2):
	"""
	:param tuple1: Object of type tuple.
	:param tuple2: Object of type tuple.
	:type tuple1: tuple
	:type tuple2: tuple
	:return: returns tuples that contains all the pairs that can be created from all the elements of tuple that were passed as arguments.
	rtype: tuple
	"""
	list_to_return = []
	
	for t1_element in tuple1:
		for t2_element in tuple2:
			list_to_return.append((t1_element, t2_element))
			list_to_return.append((t2_element, t1_element))
	
	return tuple(list_to_return)
	
def main():
	first_tuple = (1, 2)
	second_tuple = (4, 5)
	print(mult_tuple(first_tuple, second_tuple))
	
	first_tuple = (1, 2, 3)
	second_tuple = (4, 5, 6)
	print(mult_tuple(first_tuple, second_tuple))
	
if __name__ == "__main__":
	main()