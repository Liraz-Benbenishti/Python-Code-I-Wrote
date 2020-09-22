from functools import reduce

def check_id_valid(id_number):
	if isinstance(id_number, str) and id_number.isnumeric():
		try:
			id_number = int(id_number)
		except TypeError as e:
			raise TypeError("Couldn't convert into integer.")
			
	if not isinstance(id_number, int):
		raise TypeError("The input you inserted isn't of type integer")
	
	if id_number > 999999999 or id_number < 100000000:
		raise ValueError("The number is out of bound [100000000-999999999]")
	
	# Assume here that number is integer with 9 digits:
	id_list = integer_to_list(id_number)
	mult = map(lambda x , y: x * y, id_list, [1, 2, 1, 2, 1, 2, 1, 2, 1])
	mult2 = map(lambda x: int(x/10) + x % 10, mult)
	sum = reduce(lambda x, y: x + y, mult2, 0)
	#print(sum)
	if sum % 10 == 0:
		return True
	return False

class IDIterator:
	def __init__(self, id = 0):
		self._id = id
		
	def __iter__(self):
		return self
		
	def __next__(self):
		if self._id > 999999999:
			raise StopIteration("ID number out of bound [100000000-999999999]")
		
		while not check_id_valid(self._id):
			self._id += 1
			if self._id > 999999999:
				raise StopIteration("ID number out of bound [100000000-999999999]")
		valid_id = self._id
		self._id += 1
		return valid_id
	
def integer_to_list(number):
	id_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	index = 0
	while number > 0:
		id_list[8 - index] = number % 10
		index += 1
		number //= 10
	
	return id_list

def id_generator(id_number):
	id_number += 1
	while id_number <= 999999999:
		try:
			if check_id_valid(id_number):
				yield id_number
		except StopIteration:
			raise StopIteration("The number is out of bound [100000000-999999999]")
		except Exception:
			id_number += 1
			continue
		id_number += 1
	#if id_number > 999999999:
		#raise StopIteration("The number is out of bound [100000000-999999999]")
	
def main():
	id_gen = id_generator(89999999)
	for i in range(10):
		print(next(id_gen))

	id_gen = id_generator(99000000)
	for i in range(10):
		print(next(id_gen))

	id_iter = iter(IDIterator(99000000)) # 123456780
	for i in id_iter:#range(10):
		print(next(id_iter))
	
	id_iter = iter(IDIterator(0)) # 123456780
	print(next(id_iter))
	
	#print(check_id_valid(123456780))
	#print(check_id_valid(123456782))

	input_list = ["009090929", "", "123456789", 123456789.00, 123456789.09, 1, [], -1, 123456780, 123456782]
	for input in input_list:
		try:
			print(check_id_valid(input))
		except Exception as e:
			print(e)

if __name__ == "__main__":
	main()