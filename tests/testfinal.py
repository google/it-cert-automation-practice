#!/usr/bin/env python3

import csv
import datetime
import requests

# URL-ul fișierului CSV cu angajați și date de început
FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Solicită de la utilizator o dată de început."""
    print('\nGetting the first start date to query for.')
    print('The date must be greater than Jan 1st, 2018\n')

    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Descarcă fișierul CSV și returnează rândurile ca listă."""
    response = requests.get(url)
    lines = response.text.strip().split('\n')
    return lines

def get_same_or_newer(start_date):
    """
    Returnează data minimă (egala sau mai mare decât `start_date`)
    și lista angajaților care au început atunci.
    """
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])  # Ignoră antetul

    min_date = datetime.datetime.max  # Inițial o dată foarte mare
    min_date_employees = []

    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')

        if row_date < start_date:
            continue

        if row_date < min_date:
            min_date = row_date
            min_date_employees = []

        if row_date == min_date:
            full_name = f"{row[0]} {row[1]}"
            min_date_employees.append(full_name)

    return min_date, min_date_employees

def list_newer(start_date):
    """Iterează prin date și afișează angajații care au început începând cu `start_date`."""
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        if not employees:
            break
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        start_date += datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()