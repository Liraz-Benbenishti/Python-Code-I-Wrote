def callStopIteration():
	raise StopIteration

def callZeroDivisionError():
	u = 0 / 0

def callAssertionError():
	assert 0 > 1

def callImportError():
	from os import t

def callKeyError():
	mydict = {"k" : 0}
	print(mydict["u"])

"""def callSyntaxError():
	y = 0 . 0"""

"""def callIndentationError():
noindent = 0"""

def callTypeError():
	i = 5 + "y"
	
def main():
	#callStopIteration()
	#callZeroDivisionError()
	#callAssertionError()
	#callImportError()
	#callKeyError()
	#callSyntaxError()
	#callIndentationError()
	callTypeError()
	
if __name__ == "__main__":
	main()