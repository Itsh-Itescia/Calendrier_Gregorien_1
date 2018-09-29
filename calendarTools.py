# monthToString => Get month in number and return a string
# monthAdd      => Return the value to add
# yearAdd       => same but with the year
# lastDigit     => get the last digit of year
# bissextile    => Check if the year is bissextile
# dayWeek       => convert the value into a string


def monthToString(month):
    stringMonth = [
        "Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet",
        "Août", "Septembre", "Octobre", "Novembre", "Decembre"
    ]
    return stringMonth[month - 1]


def monthAdd(month):
    monthAdd = [
        0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5
    ]
    return monthAdd[month - 1]


def yearAdd(year):
    yearAdd = {
        16: 6, 17: 4, 18: 2, 19: 0, 20: 6, 21: 4
    }
    print(int(str(year)[:2]));
    return yearAdd[int(str(year)[:2]) + 1]


def lastDigit(year):
    return int(str(year)[-3:]) if '.' in str(year)[-2] else int(str(year)[-2:])


def bissextile(year):
    bissextile = False
    if year % 400 == 0:
        bissextile = True
    elif year % 100 == 0:
        bissextile = False
    elif year % 4 == 0:
        bissextile = True
    return bissextile

def dayWeek(year):
    day = [
        "Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"
    ]
    return day[year]
