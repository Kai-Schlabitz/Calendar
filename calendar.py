"""This Program allows user to enter a year and a month and display its repectivite calender.
The Program is based on a concept called Zeller's Congruence """

import sys


def print1(i, a, b):  # Defining Function for 1st print statement
    if i == 1:
        print(" " * a, i, end="  ")
    elif 1 < i < 10:
        print(" ", i, end=" ")
    if i == b:
        print("\n", end="")


def print2(i, a, b, c):  # Defining Function for 2nd print statement
    if i == 1:
        print(" " * a, i, end="  ")
    elif 1 < i < 10:
        print(" ", i, end=" ")
    if i == b or i == c:
        print("\n", end="")


def print3(i, a, b, c):  # Defining Function for 3rd print statement
    print("", i, end=" ")
    if i == a or i == b or i == c:
        print("\n", end="")


def main():
    # taking A year from the user
    year = int(input("Enter the year of which calender is required: "))

    # taking A month from the user
    month = int(input("Enter the month of which calender is required: "))

    month_is_invalid = not 1 <= month <= 12
    if month_is_invalid:
        print("Please only enter a number between 1 and 12 for the month.")
        sys.exit()

    # A dict for the number of days present in a month
    month_day_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # adjust the number of days in february for leap years
    year_is_leap_year = year % 4 == 0
    if year_is_leap_year:
        days[2] = 29

    days = month_day_dict[month]  # the number days present in the chosen month

    # In the concept of Zeller congruence,
    # January is counted as the 11th month of the last year,
    # February is the 12th month of the last year,
    # and March is the 1st month of the current year.
    if month == 1:
        year -= 1
        month = 11
    elif month == 2:
        year -= 1
        month = 12
    elif month > 2:
        month -= 2

    # https://en.wikipedia.org/wiki/Zeller%27s_congruence
    # Calculations below are based on zeller congruence
    m = (13 * month - 1) // 5
    d = year % 100
    c = year // 100
    third = d // 4
    fourth = c // 4
    fifth = 2 * c

    monday, tuesday, wednesday, thursday, friday, saturday, sunday = (
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    )

    weekdays = (sunday, monday, tuesday, wednesday, thursday, friday, saturday)

    equation = (1 + m + d + third + fourth - fifth) % 7
    weekdays[equation].append(1)

    print("Sun Mon Tue Wed Thu Fri Sat")  # printing Header of the calender
    # Printing The Calender!!!!!!!!!!
    for i in range(1, 10):
        if 1 in sunday:
            print("", i, end="  ")
            if i == 7:
                print("\n", end="")

        elif 1 in monday:
            print1(i, 4, 6)

        elif 1 in tuesday:
            print1(i, 8, 5)

        elif 1 in wednesday:
            print1(i, 12, 4)

        elif 1 in thursday:
            print1(i, 16, 3)

        elif 1 in friday:
            print2(i, 20, 2, 9)

        elif 1 in saturday:
            print2(i, 24, 1, 8)

    for i in range(10, days + 1):
        if 1 in sunday:
            print("", i, end=" ")
            if i in (7, 14, 21, 28):
                print("\n", end="")

        elif 1 in monday:
            print3(i, 13, 20, 27)

        elif 1 in tuesday:
            print3(i, 12, 19, 26)

        elif 1 in wednesday:
            print3(i, 11, 18, 25)

        elif 1 in thursday:
            print3(i, 10, 17, 24)

        elif 1 in friday:
            print3(i, 16, 23, 30)

        elif 1 in saturday:
            print3(i, 15, 12, 29)


if __name__ == "__main__":
    main()
