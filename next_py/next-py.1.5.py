#import functools
with open('names.txt', 'r') as file:
	#print(functools.reduce(max, file.read().split("\n")))
	#print(sum([len(num) for num in file.read().split("\n")]))
	#print(len("".join(file.read().split("\n"))))
	#list = sorted(file.read().split("\n"), key=len)
	#print("\n".join([x for x in list if len(x) == len(list[0])]))
	#with open('name_length.txt', 'w') as name_length:
	#	name_length.write("\n".join([str(len(x)) for x in file.read().split("\n")]))
	length = int(input("Enter name length: "))
	print("\n".join([x for x in file.read().split("\n") if len(x) == length]))