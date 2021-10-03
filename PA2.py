#Chris Plowman
#CS-151, Dr. Rajeev
#Program assignment 2
#10/3/2021

# 30 days has september, april, june, and november.
# All the rest have 31, but feb is 28.
# The leap year, which comes once in 4 gives feb one day more.

month = int(input("Enter the month (number 1-12): "))
year = float(input("Enter the year: "))

leap_year = False
#if (year % 100) == 0 and (year % 400) == 0:
if year % 4 == 0:
    if year % 100 > 0:
        leap_year = True
    elif year % 400 == 0:
        leap_year = True
print("leap_year:", leap_year)

days = 31
if month == 4 or month == 6 or month == 9 or month == 11:
    days = 30
elif month == 2:
    days = 28
    if leap_year == True:
        days = 29

print("There are", days, "days in month", month, sep = " ")

