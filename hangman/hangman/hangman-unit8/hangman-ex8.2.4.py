def sort_anagrams(list_of_strings):
	"""
	:param list_of_strings: list of strings, where each string is one word.
	:type list_of_strings: list
	:return: return a list of those strings, the list is devided to lists where the inner list is containing words that are anagrams of one another
	rtype: 
	"""
	list_to_return = []
	for string in list_of_strings:
		index = -1
		for i in range(len(list_to_return)):
			list = list_to_return[i]
			is_found = True
			for char in string:
				if (char not in list[0] or list[0].count(char) != string.count(char)):
					is_found = False
					break
			if (is_found):
				list.append(string)
				index = 0
				break
							
		if (index == -1):
			list_to_return.append([string])
	
	return list_to_return
	
def main():
	list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
	print(sort_anagrams(list_of_words))
	
if __name__ == "__main__":
	main()