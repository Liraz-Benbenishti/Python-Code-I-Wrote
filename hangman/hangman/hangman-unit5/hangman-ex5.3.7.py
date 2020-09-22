def chocolate_maker(small, big, x):
	if(x == 0):
		return True
	elif (small == 0 and big == 0):
		return False
	if (small > 0):
		return chocolate_maker(small - 1, big, x) or chocolate_maker(small - 1, big, x - 1) 
	if (big > 0):
		return chocolate_maker(small, big - 1, x) or chocolate_maker(small, big - 1, x - 5)
	return

def chocolate_maker2(small, big, x):
		m = x % 5
		n = (x - m) / 5
		if (big >= n and small >= m):
			return True
		if (big < n and small < m):
			return False
		if (big < n and small >= m):
			return small >= m + 5 * (n - big)
		if (big >= n and small < m):
			return ((m - small) % 5 == 0) and (big >= n + ((m - small) / 5))
		
for small in range(0, 10):
	for big in range(0, 10):
		for x in range(0, 65):
			if (chocolate_maker(small, big, x) != chocolate_maker2(small, big, x)):
				print(small, big, x, chocolate_maker(small, big, x), chocolate_maker2(small, big, x))
print("FINISH!")

print(chocolate_maker2(3, 1, 8))

print(chocolate_maker2(3, 1, 9))

print(chocolate_maker2(3, 2, 10))