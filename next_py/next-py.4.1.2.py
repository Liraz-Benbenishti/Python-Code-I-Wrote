def translate(sentence):
	words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
	translate_generator = (words[i] for i in sentence.split(' '))
	ret_lst = []
	for string_generator in translate_generator:
		ret_lst.append(string_generator)
	ret_str = " ".join(ret_lst)
	return ret_str
	
def main():
	print(translate("el gato esta en la casa"))
	
if __name__ == "__main__":
	main()