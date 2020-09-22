from functools import reduce

def add_dbl_char(list, char):
	list.append(char * 2)
	return list

def double_letter(my_str):
	"""
	:param my_str: string to change.
	:type my_str: string
	:return: a new string that built from two double appearance of each char in the string.
	rtype: string
	"""
	return "".join(list(reduce(add_dbl_char, list(my_str), [])))
	

def main():
	print(double_letter("python"))
	print(double_letter("we are the champion!"))

if __name__ == "__main__":
	main()