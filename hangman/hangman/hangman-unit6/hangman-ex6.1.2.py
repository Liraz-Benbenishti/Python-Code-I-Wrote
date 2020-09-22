def shift_left(my_list):
	""""
	The function gets a list of length 3 and return new list shifted one step to the left.
	:param my_list: The list to be shifted.
	:type my_list: list
	:return: the list shifted to the left.
	rtype: list.
	"""
	new_list = my_list[1:] + my_list[0:1] #[my_list[1], my_list[2], my_list[0]]
	print(new_list)
	return new_list
	

def main():
	shift_left([0, 1, 2])
	shift_left(['monkey', 2.0, 1])
	
if __name__ == "__main__":
	main()
	