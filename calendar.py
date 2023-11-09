"""This Program allows user to enter a year and a month and display its repective calender.
The Program is based on a concept called Zeller's Congruence """
# https://en.wikipedia.org/wiki/Zeller%27s_congruence

import sys


def get_user_input():
    """
    This function asks the user for the year and month of the calendar that
    should be generated. It then makes sure that the month is a number
    between 1 and 12 and returns the year and the month.
    """
    input_year = int(input("Enter the year of which calender is required: "))
    input_month = int(input(
    "Enter the month of which calender "
    "is required as a number between 1 and 12: "
    ))

    month_is_invalid = not 1 <= input_month <= 12
    if month_is_invalid:
        print("Please only enter a number between 1 and 12 for the month.")
        sys.exit()

    return input_year, input_month


def get_weekday_of_first_day_of_month(year, month):
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
    else:
        month -= 2

    years_per_century = 100
    leap_year_period = 4

    # day of month
    q = 1

    # Calculations below are based on zeller congruence
    # https://en.wikipedia.org/wiki/Zeller%27s_congruence
    # year of century
    K = year % years_per_century

    # zero based century
    J = year // years_per_century
    # The zero based century of a year just chops off the last two digits.
    # For example it is 20 for the year 2000 but 19 for 1999.

    
    leap_year_offset = K // leap_year_period
    weekday_progression_offset = J // leap_year_period - 2 * J

    # this term adjusts for the variation in the days of the month
    M = (13 * month - 1) // 5

    weekday = (q + M + K + leap_year_offset + weekday_progression_offset) % 7

    return weekday


def get_days_in_month(year, month):
    # adjust the number of days in february for leap years
    year_is_leap_year = year % 4 == 0

    month_day_dict = {
        1: 31,
        2: 28 + int(year_is_leap_year),
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    days = month_day_dict[month]
    return days


def print_calendar(first_day_weekday, days_in_month):
    days_in_week = 7
    first_row_days = days_in_week - first_day_weekday
    last_row_overhang = (days_in_month - first_row_days) % days_in_week

    calendar_boxes = (
        [' '] * first_day_weekday
        + list(range(1, days_in_month + 1))
        + [' '] * last_row_overhang
    )

    weekday_labels = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
    print(*weekday_labels, sep='\t')  # printing Header of the calender
    
    for row in range(0, len(calendar_boxes), days_in_week):
        for box in calendar_boxes[row : row + days_in_week]:
            print(f"{box:>3}", end='\t')
        print()

def main():
    year, month = get_user_input()
    
    first_day_weekday = get_weekday_of_first_day_of_month(year, month)

    days_in_month = get_days_in_month(year, month)

    print_calendar(first_day_weekday, days_in_month)

if __name__ == "__main__":
    main()
