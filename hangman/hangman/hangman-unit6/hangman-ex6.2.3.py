def format_list(my_list):
	"""
	The function gets a even-lengthed list.
	The function returns a string that contains the list elements in the even indices seperated by comma and space, and the last element with 'and' before it.
	:param my_list: List to format.
	:type my_list: list
	:return: string of even-index list elements.
	rtype: string
	"""
	return ", ".join(my_list[::2]) + (" and " + my_list[-1])
	
def main():
	my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
	print(format_list(my_list))	

if __name__ == "__main__":
	main()