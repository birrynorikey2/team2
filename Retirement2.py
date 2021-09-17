import re
import math
import sys
import calendar


def getData():

    b_year = input("Enter the year of birth in YYYY format or press Enter to exit: ")
    if b_year == "":
        sys.exit()
    b_year = int(b_year)
    b_month = int(input("Enter the month of birth: "))

    birth = [b_year, b_month]

    return birth
# separated the different functions to make it more modular?

def r_calc(passed_list):

    year = passed_list[0]
    month = passed_list[1]
    plus = 0

    if year <= 1937:
        age = 65
    elif 1937 < year <= 1943:
        age = 65
        plus = 2 * (year - 1937)
    elif 1942 < year <= 1954:
        age = 66
    elif year < 1960:
        age = 66
        plus = 2 * (year - 1954)
    else:
        age = 67

    if plus != 0:
        print("Your full retirement age is: ", age, " and ", plus, " months")
    else:
        print("Your full retirement age is: ", age)

    # I thought it would be cleaner to not have 0 months so I made a if then statement.

    birth = [year, month, age, plus]

    return birth


def r_date(passed_list):
    
    year = passed_list[0]
    month = passed_list[1]
    age = passed_list[2]
    plus = passed_list[3]

    if month + plus <= 12:
        print("This will be in", calendar.month_name[month + plus], "of", year + age)
    else:
        print("This will be in", calendar.month_name[month + plus - 12], "of", year + age + 1)

    # we need an if statement in case the birth month + the retirement month add up to a year.


def main():
    print("Social Security Full Retirement Age Calculator")
    while True:
        birth_list = getData()
    # gets birth month and year into a list
        birth_list = r_calc(birth_list)
    # throws list into calculator to determine retirement age
        r_date(birth_list)
    # throw a new version of the birth list into r_date to find the date of retirement
        print()


main()

