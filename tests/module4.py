#!/usr/bin/env python3

import csv
import datetime

# Local file path for the CSV with employees and start dates
FILE_PATH = r"C:\Users\INVIBES\Downloads\employees-with-date.csv"

def get_start_date():
    """Solicită de la utilizator o dată de început."""
    print('\nGetting the first start date to query for.')
    print('The date must be greater than Jan 1st, 2018\n')

    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(file_path):
    """Citește fișierul CSV local și returnează rândurile ca listă."""
    with open(file_path, encoding="utf-8") as f:
        lines = f.read().strip().split('\n')
    return lines

def list_newer(start_date):
    """Afișează angajații care au început începând cu `start_date`, ordonați după dată."""
    data = get_file_lines(FILE_PATH)  # Read file once
    reader = csv.reader(data[1:])  # Ignoră antetul

    # Creează o listă de tuple (date, full_name) pentru angajații cu date >= start_date
    employees = []
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%m/%d/%Y')
        if row_date >= start_date:
            full_name = f"{row[0]} {row[1]}"
            employees.append((row_date, full_name))

    # Sortează după dată
    employees.sort()

    # Grupează și afișează angajații după dată
    last_date = None
    names = []
    for row_date, full_name in employees:
        if last_date is None or row_date != last_date:
            if names:
                print("Started on {}: {}".format(last_date.strftime("%b %d, %Y"), ", ".join(names)))
            last_date = row_date
            names = [full_name]
        else:
            names.append(full_name)
            
    if names:
        print("Started on {}: {}".format(last_date.strftime("%b %d, %Y"), ", ".join(names)))

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()