def arrow(my_char, max_length):
	"""
	:param my_char: Single char.
	:param max_length: Maximum size.
	:type my_char: string
	:type max_length: int
	:return: returns a string that symbolize a structure of an arrow, built from the input char, the middle of the arrow is of length of the input max_length.
	rtype: string
	"""
	string_list = []
	for i in range(1, max_length+1, 1):
		for j in range(0, i, 1):
			string_list.append(my_char + " ")
		string_list.append("\n")
	
	for i in range(max_length-1, 0, -1):
		for j in range(0, i, 1):
			string_list.append(my_char + " ")
		string_list.append("\n")			
	return "".join(string_list)
	
def main():
	print(arrow("*", 5))
	
if __name__ == "__main__":
	main()