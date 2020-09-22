def are_lists_equal(list1, list2):
	"""
	The function gets two lists that contain elements of types int and float only.
	The function return True if the two lists contain exactly the same elements (even if the order is different), otherwise, return False.
	:param list1: The first list.
	:param list2: The second list.
	:type list1: list
	:type list2: list
	:return: The function return true if the lists contains the same elements exactly.
	rtype: bool
	"""
	return sorted(list1) == sorted(list2)
	
def main():
	list1 = [0.6, 1, 2, 3]
	list2 = [3, 2, 0.6, 1]
	list3 = [9, 0, 5, 10.5]
	print(are_lists_equal(list1, list2))
	print(are_lists_equal(list1, list3))
	
if __name__ == "__main__":
	main()