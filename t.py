from datetime import date
from dateutil import relativedelta

date1 = date(2018,7,4)
date2 = date(2020,8,8)

diff = relativedelta.relativedelta(date2, date1)
years = diff.years
months = diff.months
days = diff.days

print(f'years: {years} -- months: {months} -- days: {days}')