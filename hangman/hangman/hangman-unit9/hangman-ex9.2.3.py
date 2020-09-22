def who_is_missing(file_name):
	"""
	:param file_name: path to text file.
	:type file_name: string
	:return: the missing number.
	rtype: int
	"""
	with open(file_name) as numbers_file:
		string_of_numbers = numbers_file.read().splitlines()[0]
		list_of_numbers = [int(x) for x in sorted(string_of_numbers.split(","))]
		compare_num = 1
		for num in list_of_numbers:
			if (num == compare_num):
				compare_num = compare_num + 1
			else:
				with open(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\found.txt", 'w') as output_file:
					output_file.write(str(compare_num))
				break
	
def main():
	who_is_missing(r"C:\Users\Liraz\Desktop\hangman\hangman-unit9\findMe.txt")

if __name__ == "__main__":
	main()