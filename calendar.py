# checkDate      => check if the date is valid
# main           => main function who get the input from the user and call the other functions
# georgianCalcul => do the georgian calcul to get the day.

from calendarTools import *
import re


def checkDate(day, month, year):
    if day < 1 or day > 31:
        return False
    if month < 1 or month > 12:
        return False
    if year <= 1582 or year >= 2100:         # Check if year is after the first November of 1582 and valid
        if year == 1582 and month >= 10:
            return True
        return False
    return True


def georgianCalcul(day, month, year):
    lastDigitYear = lastDigit(year) // 4
    quarterYear = lastDigitYear // 4
    lastDigitYear += quarterYear
    lastDigitYear += day
    monthResult = monthAdd(month)
    lastDigitYear += monthResult

    if bissextile(year) is True and month <= 2:
        lastDigitYear -= 1
    yearResult = yearAdd(year)
    lastDigitYear += yearResult
    yearRest = lastDigitYear % 7

    dayString = dayWeek(yearRest)
    print("The day in georgian format of ", day, "/", month, "/", year, " is : ", dayString)


def main():
    done = False

    while done is False:
        date = input("Enter a valid date in this format JJ/MM/AAAA\n")

        # regex to know if the date is in valid format
        if re.match(r"\s*\d{1,2}\s*/\s*\d{1,2}\s*/\s*\d{4}\s*", date) is not None:
            date.strip()
            date.replace(" ", "")
            day, month, year = date.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            if checkDate(day, month, year) is False:
                done = False
            else:
                done = True
        if done is False:
            print("Your format is not valid (enter a date between 1/10/1582 and 31/12/2099)\n")
    day, month, year = date.split("/")
    day = int(day)
    month = int(month)
    year = int(year)
    georgianCalcul(day, month, year)


main()
