def longest(my_list):
	"""
	The function gets a list that contains strings.
	The function returns the longest list.
	:params my_list: The list we are checking.
	:type my_list: list
	:return: Return the longest string.
	rtype: string
	"""
	return sorted(my_list, key=len)[-1]
	
def main():
	list1 = ["111", "234", "2000", "goru", "birthday", "09"]
	print(longest(list1))
	
if __name__ == "__main__":
	main()
	
