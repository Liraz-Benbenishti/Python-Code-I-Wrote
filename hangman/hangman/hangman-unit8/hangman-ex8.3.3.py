def count_chars(my_str):
	"""
	:param my_str: gets a string as parameter
	:type my_str: string
	:return: returns a dictionary, where each element in it is a pair of key, char from the string, and value, number of appearance the char have in the string.
	rtype: dictionary
	"""
	string_dict = {}
	for char in my_str:
		if (char.isalpha()):
			string_dict[char] = my_str.count(char)
	
	return string_dict
	
def main():
	magic_str = "abra cadabra"
	print(count_chars(magic_str))
	
if __name__ == "__main__":
	main()