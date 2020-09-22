def read_file(file_name):
	"""
	The function checks if the file exists or not, and if it does returns its content.
	:param file_name: The name of the file.
	:type file_name: string
	:rtype: string
	:return: Returns a string with the file content or a error message.
	"""
	ret_str = "__CONTENT_START__\n"
	try:
		f = open(file_name, "r")
		try:
			lines = f.readlines()
		finally:
			f.close()
	except IOError:
		ret_str = ret_str + "__NO_SUCH_FILE__\n"
	else:
		for line in lines:
			ret_str = ret_str + line
		ret_str = ret_str + "\n"
	finally:
		ret_str = ret_str + "__CONTENT_END__"
	return ret_str

def main():
	EXISTING_FILE = "existing.txt"
	NOT_EXISTING_FILE = "not_existing.txt"
	
	print(read_file(EXISTING_FILE))
	print(read_file(NOT_EXISTING_FILE))
	
if __name__ == "__main__":
	main()