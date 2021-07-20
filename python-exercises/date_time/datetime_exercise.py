# This file includes exercise for datetime section
import pytz

from datetime import datetime as dt


def get_current_time():
    """
    Get the current date, datetime and print out to the screen
    """
    print(f"Current date: {dt.now().date()}")
    print(f"Current date time: {dt.now()}")


def get_UTC_GMT_now(timezone):
    """
    Get the current datetime of the timezone `GMT +7` and convert it into `UTC`, `GMT` and print out to the screen.
    """
    current_date_time = dt.now(pytz.timezone(timezone))
    print(f"UTC: {current_date_time.astimezone(pytz.UTC)}")
    print(f'GMT: {current_date_time.astimezone(pytz.timezone("GMT"))}')


def convert_date_format(date):
    """
    Convert the following date string into date and print out as following format `dd/mm/yyyy`
    """
    print(dt.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y"))


if __name__ == "__main__":

    # Exercise 1
    get_current_time()

    # Exercise 2
    get_UTC_GMT_now("Etc/GMT+7")

    # Exercise 3
    convert_date_format("2021-07-04")
