def get_fibo():
	x = 0
	y = 1
	while True:
		yield x
		temp = x
		x = y
		y = temp + y
	
def main():
	fibo_gen = get_fibo()
	for i in range(10):
		print(next(fibo_gen))

if __name__ == "__main__":
	main()