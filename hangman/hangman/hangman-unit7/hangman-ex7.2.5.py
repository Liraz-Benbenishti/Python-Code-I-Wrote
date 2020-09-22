def sequence_del(my_str):
	"""
	:param my_str: string before editing.
	:type my_str: string
	:return: the string after deleting duplicate letters.
	rtype: string
	"""
	list_of_letters = [my_str[0]]
	for char in my_str:
		if (list_of_letters[-1] != char):
			list_of_letters.append(char)
	return "".join(list_of_letters)
	
def main():
	print(sequence_del("ppyyyyythhhhhooonnnnn"))
	print(sequence_del("SSSSsssshhhh"))
	print(sequence_del("Heeyyy   yyouuuu!!!"))

if __name__ == "__main__":
	main()