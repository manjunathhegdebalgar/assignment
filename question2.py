""" Program to calculate the number of days between two dates"""

from datetime import date
import sys

max_date = str(input("Enter the maximum date in YYYYMMDD format"))
min_date = str(input("Enter the minimum date in YYYYMMDD format"))
# Following lines split the dates at proper positions to fetch year, month and day.
max_year = int(max_date[:4])
max_month = int(max_date[4:6])
# Checking for the error in month
if max_month == 0 or max_month > 12:
    print("Error in the month of maximum date")
    sys.exit(0)
max_day = int(max_date[6:8])
# Checking for error in day
if max_day == 0 or max_day > 31:
    print("Error in the day of maximum date")
    sys.exit(0)
min_year = int(min_date[:4])
min_month = int(min_date[4:6])
# Checking for error in month
if min_month == 0 or min_month > 12:
    print("Error in the month of minimum date")
    sys.exit(0)
# Checking for error in day
min_day = int(min_date[6:8])
if min_day == 0 or min_day > 31:
    print("Error in the day minimum date")
    sys.exit(0)
max_date = date(
    max_year, max_month, max_day
)  # Preparing max_date for inbuilt date function
min_date = date(
    min_year, min_month, min_day
)  # Feeding min_date for inbuilt date function
difference_in_days = max_date - min_date
print("The number of days between given two dates are", difference_in_days)
