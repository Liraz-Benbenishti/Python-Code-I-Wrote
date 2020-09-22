def parse_ranges(ranges_string):
	"""
	:params ranges_string: String that represent range of numbers.
	:type ranges_string: string
	:return: Generator that generate all the numbers in that range.
	:rtype: generator
	"""
	generate_ranges_strings = ([i.split("-")[0], i.split("-")[1]] for i in ranges_string.split(","))
	generate_numbers = (num for start, stop in generate_ranges_strings for num in range(int(start), int(stop)+1))
	return generate_numbers
	#generate_range = (for i in range(range_tpl, range_tpl+1) for range_tpl in generate_ranges_strings)
	#return generate_range

def main():
	print(list(parse_ranges("1-2,4-4,8-10")))
	print(list(parse_ranges("0-0,4-8,20-21,43-45")))

if __name__ == "__main__":
	main()