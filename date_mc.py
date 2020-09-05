#!/usr/bin/env python3
from datetime import date


class Date:
    def __init__(self, month_to_check, initial_month, final_month):
        self.month_to_check = month_to_check
        self.initial_month = initial_month
        self.final_month = final_month
        self.today = date.today()

    @property
    def selected_date(self):
        selected_date = date(year=self.today.year, month=self.month_to_check, day=1)
        if self.initial_month > self.month_to_check:
            selected_date = date(year=self.today.year + 1, month=self.month_to_check, day=1)
        return selected_date

    @property
    def initial_date(self):
        initial_date = date(self.today.year, self.initial_month, 1)
        return initial_date

    @property
    def final_date(self):
        final_date_year = self.today.year + 1 if self.initial_month > self.final_month else self.today.year
        final_date = date(final_date_year, self.final_month, 1)
        return final_date

    def is_between(self):
        return self.initial_date <= self.selected_date <= self.final_date


def main():
    month_to_check = int(input('Enter the month number to check: '))
    initial_month = int(input('Enter the initial month: '))
    final_month = int(input('Enter the final month: '))
    date_mc = Date(month_to_check, initial_month, final_month)
    print(date_mc.is_between())


if __name__ == '__main__':
    main()

