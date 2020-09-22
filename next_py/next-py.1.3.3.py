import functools

def is_funny(string):
    #for char in string:
    #    if char != 'h' and char != 'a':
    #        return False
    #return True
    return True in [False if char != 'h' and char != 'a' else True for char in string]
	
def main():
	print(is_funny("hahahahahaha"))
	print(is_funny("not funny"))

if __name__ == "__main__":
	main()