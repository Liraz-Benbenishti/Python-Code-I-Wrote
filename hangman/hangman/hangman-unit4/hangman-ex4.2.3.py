temperature = input("Insert the temperature you would like to convert: ")
temperature = temperature.upper()

letter = ""

if ("C" in temperature):
	# Convert to Furnheit
	celcius = float(temperature[:temperature.find("C")])
	result = (9 * celcius + (32 * 5)) / 5
	letter = "F"
elif ("F" in temperature):
	# Convert to Celcius
	fuhrneit = float(temperature[:temperature.find("F")])
	result = (5 * fuhrneit - 160) / 9	
	letter = "C"

if (result % 1 == 0):
	result = int(result)

print(str(result) + letter)