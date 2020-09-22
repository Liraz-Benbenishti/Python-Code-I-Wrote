from functools import reduce

ID_MAX_NUMBER = 999999999
ID_MIN_NUMBER = 100000000

def check_id_valid(id_number):
	"""
	Checks if the input string is a legitimate integer.
	:param id_number: input that suppose to be an integer.
	:type id_number: should be an integer.
	:return: Return if the integer is valid or not.
	:rtype: bool
	:raise: TypeError: raises an Exception
	:raise: ValueError: raises an Exception
	"""
	if isinstance(id_number, str) and id_number.isnumeric(): # Check if the num is a string chk if it's a numeric str.
		id_number = int(id_number) # Try to convert the numeric string to type integer.
			
	if not isinstance(id_number, int): # Check if the number is not of type integer.
		raise TypeError("The input you inserted isn't of type integer. type: %s" % type(id_number)) #throw an exception
	
	if id_number > ID_MAX_NUMBER: # Check if the number is longer than 9 digits.
		raise ValueError("The number %s is longer than 9 digits!" % str(id_number)) # throw a ValueError exception.
	if id_number < ID_MIN_NUMBER: # Check if the number is shorter than 9 digits.
		raise ValueError("The number %s is shorter than 9 digits!" % str(id_number)) # throw a ValueError exception.
	
	# If the execution got to this code, than id_number is a 9-digit integer.
	id_list = integer_to_list(id_number) # Convert the number to a list of digits.
	mult = map(lambda x , y: x * y, id_list, [1, 2, 1, 2, 1, 2, 1, 2, 1]) # Calculate the multiplications.
	mult2 = map(lambda x: int(x/10) + x % 10, mult) # Add digits of numbers larger than 9 together.
	sum = reduce(lambda x, y: x + y, mult2, 0) # Add all the numbers in the list together.
	
	if sum % 10 == 0: # Check if the number is divisible by 10.
		return True # If so, the number is a valid id number - return True.
	return False # Else, the number is not a valid id number - return False.

class IDIterator:
	"""
	A class used to define the iterator of valid id numbers.
	"""
	def __init__(self, id = 123456780):
		"""
		Initialize an object of type IDIterator.
		:param id: the id_number to start the iterator from.
		:type id: integer
		:return: None
		:rtype: None
		"""
		self._id = id # Initialize the iterator's id variable.
			
	def __iter__(self):
		"""
		Returns a reference to the iterator.
		:return: Retruns the iterator.
		:rtype: Returns a reference to the iterator (IDIterator).
		"""
		return self # Return the iterator.
		
	def __next__(self):
		"""
		Returns the next valid id number.
		:return: Returns the next valid id number.
		:rtype: integer
		:raise: StopIteration: raises an Exception
		"""
		
		check_id_valid(self._id) # Running this function just to guarantee input is valid before processing in loop.
		
		while self._id <= ID_MAX_NUMBER: # While loop as long as number is smaller than 999999999 (9 digits).
			if not check_id_valid(self._id): # Checks if the number is not a valid id number.
				self._id += 1 # Add one to the value of the number.
			else:
				break

		if self._id > ID_MAX_NUMBER: # if the number id is larger than 999999999, it's out of bound.
			raise StopIteration("No more valid ID numbers!") # throw a StopIteration exception.
			
		ret_value = self._id # Store the vlaue to return.
		self._id += 1 # Add one to the value of the number.
		return ret_value # Return the next valid id number.
	
def integer_to_list(number):
	"""
	Get a 9-digits number and make a list of its digits.
	:param number: 9-digit number to turn into a list.
	:type number: integer
	:return: list of the number digits.
	:rtype: list
	"""
	id_list = [0, 0, 0, 0, 0, 0, 0, 0, 0] # List to hold and return the id digits.
	index = 0 # Index of element in the list.
	while number > 0: # While loop as long as number is larger than 0.
		id_list[8 - index] = number % 10 # Put the digit in the right place in the digit list.
		index += 1 # Increade index by 1.
		number //= 10 # Divide without remainder the number by 10. (to move to the next digit).
	
	return id_list # Return the list of digits.

def id_generator(id_number):
	"""
	Yields the next valid id numbers after the input number.
	:param id_number: number to generate the next valid id number from.
	:type id_number: integer
	:yield: the next valid id number
	:ytype: integer
	:raise: StopIteration: When the generator stop running, it's automatically raise an exception.
	"""
	check_id_valid(id_number) # Running this function just to guarantee the input is valid before processing in loop.
	
	while id_number <= ID_MAX_NUMBER: # While loop as long as number is smaller than 999999999 (9 digits).
		if check_id_valid(id_number): # Checks if the number is a valid id number.
			yield id_number # If so, yield the valid id number.
		id_number += 1 # Incrase the number by 1.
	
def ask_input():
	"""
	Ask for an input from the user.
	:return: Returns an integer.
	:rtype: integer
	"""
	id_number = "" # Initialize the input string.
	while id_number == "": # As long the string is empty, ask for input.
		try:
			id_number = input("Please enter an ID number: ")
			check_id_valid(id_number)
			break
		except Exception as e:
			print(e) # Throws the exception error string.
			id_number = ""
	
	id_number = int(id_number) # Convert into an integer.
	return id_number

def main():	
	try:
		print(check_id_valid(123456780)) # Print if the number is a valid number or not.
	except Exception as e: # Checks if an exception have been thrown.
		print(type(e), ": ", e) # Throws the exception error string.
	
	try:
		print(check_id_valid(123456782)) # Print if the number is a valid number or not.
	except Exception as e: # Checks if an exception have been thrown.
		print(type(e), ": ", e) # Throws the exception error string.
	
	id_number = ask_input() # Ask for input from the user.
	# At this point, id_number is guarantee to be an integer with 9 digits so catching exceptions of type 
	# TypeError, ValueError is unneeded. However, I added them anyway because that's what I read is needed on the forum
	
	#id_number = 123456780 # In case I was suppose to do it like that and not with input().

	print("Generator")
	id_gen = id_generator(id_number) # Initialise the iterator.
	count_prints = 0 # Initialize the counter.
	while count_prints < 10:
		try:
			print(next(id_gen)) # Print the valid numbers.
		except StopIteration as e:
			print("No more valid ID numbers!") # Throws the exception error string.
			break
		except TypeError as e:
			print(e) # Throws the exception error string.
			break
		except ValueError as e:
			print(e) # Throws the exception error string.
			break
		else:
			count_prints+=1	

	print("Iterator")
	id_iter = iter(IDIterator(id_number)) # Initialise the iterator.
	count_prints = 0 # Initialize the counter.
	while count_prints < 10:
		try:
			print(next(id_iter)) # Print the valid numbers.
		except StopIteration as e:
			print(e) # Throws the exception error string.
			break
		except TypeError as e:
			print(e) # Throws the exception error string.
			break
		except ValueError as e:
			print(e) # Throws the exception error string.
			break
		else:
			count_prints+=1	

if __name__ == "__main__": # Checks if the code run as a script.
	main() # If so, run the main function.