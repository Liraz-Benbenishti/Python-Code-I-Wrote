import calendar

date_from_user = input("Enter a date: ") # Expected format: dd/mm/yyyy

first_slash = date_from_user.find("/")
second_slash = first_slash + date_from_user[first_slash+1:].find("/") + 1

day = int(date_from_user[:first_slash])
month = int(date_from_user[first_slash+1:second_slash])
year = int(date_from_user[second_slash+1:])

print("That date's weekday is", calendar.day_name[calendar.weekday(year, month, day)])

