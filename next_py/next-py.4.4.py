def gen_secs():
	for i in range(60):
		yield i
		
def gen_minutes():
	for i in range(60):
		yield i
		
def gen_hours():
	for i in range(24):
		yield i

def is_leap_year(year):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return True
	return False
	
def gen_days(month, leap_year = True):
	days = 30
	if month == 2 and leap_year == False:
		days = 28
	if month == 2 and leap_year == True:
		days = 29
	if month in [1, 3, 5, 7, 8, 10, 12]:
		days = 31

	for i in range(1, days + 1):
		yield i

def gen_months():
	for i in range(1, 13):
		yield i

def gen_years(start = 2019):
	while True:
		yield start
		start = start + 1

def gen_date():
	for gy in gen_years(2019):
		for gm in gen_months():
			for gd in gen_days(gm, is_leap_year(gy)):
					for gh in gen_hours():
						for gm2 in gen_minutes():
							for gs in gen_secs():
								yield "%02d/%02d/%d %02d:%02d:%02d" % (gd,gm,gy, gh,gm2,gs)


def gen_time():	
	for gh in gen_hours():
		for gm in gen_minutes():
			for gs in gen_secs():
				yield "%02d:%02d:%02d" % (gh,gm,gs)
				
def main():
	gt = gen_date()
	for i in range(10 ** 10):
		if i != 0 and i % 1000000 == 0:
			print(next(gt))
		else:
			next(gt)
			
	#for gt in gen_date():
	#	print(gt)
		
if __name__ == "__main__":
	main()