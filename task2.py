import datetime
import calendar
from art import *


def get_birthday():
    day = int(input("Введите день вашего рождения (от 1 до 31): "))
    month = int(input("Введите месяц вашего рождения (от 1 до 12): "))
    year = int(input("Введите год вашего рождения: "))
    return day, month, year


def get_age(day, month, year):
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age


def day_of_week(day, month, year,):
    date_obj = datetime.date(year, month, day)
    day_of_week_en = date_obj.strftime("%A")
    if day_of_week_en == "Monday":
        return "Понедельник"
    elif day_of_week_en == "Tuesday":
        return "Вторник"
    elif day_of_week_en == "Wednesday":
        return "Среда"
    elif day_of_week_en == "Thursday":
        return "Четверг"
    elif day_of_week_en == "Friday":
        return "Пятница"
    elif day_of_week_en == "Saturday":
        return "Суббота"
    elif day_of_week_en == "Sunday":
        return "Воскресенье"


def display_date_as_stars(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    date_str = f"{day_str} {month_str} {year_str}"
    print(text2art(date_str, font="5x7"))


def is_leap_year(year):
    return calendar.isleap(year)


def main():
    day, month, year = get_birthday()
    print(f"День недели на момент вашего рождения: {day_of_week(day, month, year)}.")
    print(f"Ваш год рождения {"является високосным" if is_leap_year(year) else "не является високосным"}.")
    print(f"Вам сейчас {get_age(day, month, year)} лет.")
    print("Ваша дата рождения в символьном формате дд мм гггг:")
    display_date_as_stars(day, month, year)


if __name__ == "__main__":
    main()