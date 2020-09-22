def extend_list_x(list_x, list_y):
	"""
	The function gets two lists.
	The function return the list_x with list_y added to its beginning.
	:param list_x: List x.
	:param list_y: List Y.
	:type list_x: list
	:type list_y: list
	return: list_x with list_Y appended to its beginning.
	rtype: list
	"""
	list_x[0:0] = list_y
	return list_x
	
def main():
	x = [4, 5, 6]
	y = [1, 2, 3]
	print(extend_list_x(x, y))

if __name__ == "__main__":
	main()