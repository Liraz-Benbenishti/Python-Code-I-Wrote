def inverse_dict(my_dict):
	"""
	:param my_dict: dictionary to reverse.
	:type my_dict: dict
	:return: returns a new dictionary with reversed mapping, every key in the dict is a value in the returned dict and every value is a key in the returned dict.
	"""
	returned_dict = {}
	for key, value in my_dict.items():
		if (value in returned_dict.keys()):
			returned_dict[value].append(key)
		else:
			returned_dict[value] = [key]

	for key in returned_dict.keys():
		returned_dict[key] = sorted(returned_dict[key])
	
	return returned_dict
	
def main():
	course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
	print(inverse_dict(course_dict))

if __name__ == "__main__":
	main()