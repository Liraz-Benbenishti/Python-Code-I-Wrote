import itertools
from functools import reduce

sets = set()
for length in range(7, 16):
	iter = itertools.combinations([20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1], length)
	for i in iter:
		s = sum(i)
		if s == 100:
			sets.add(i)
print(len(sets))
for set in sets:
	print(set)