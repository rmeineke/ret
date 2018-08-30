import math
from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
from enum import Enum
import logging
import sys
import json


def get_latest_info():
    with open("ret.json") as jsn:
        data = json.load(jsn)
    # return the last in the list ... should be most current
    return data[-1]


def construct_output_string(years, months, days):
    outputstr = ''

    if years > 1:
        outputstr = outputstr + f'{years} years'
    elif years == 1:
        outputstr = outputstr + f'{years} year'

    if months and years:
        outputstr = outputstr + f', '

    if months > 1:
        outputstr = outputstr + f'{months} months '
    elif months == 1:
        outputstr = outputstr + f'{months} month '

    if days:
        outputstr = outputstr + f'and '

    if days > 1:
        outputstr = outputstr + f'{days} days '
    elif days == 1:
        outputstr = outputstr + f'{days} day '

    outputstr = outputstr + f'left'

    return outputstr


def main():
    # set up for logging
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL,
              }
    if len(sys.argv) > 1:
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)
        logging.basicConfig(
            format='%(asctime)s - %(levelname)-8s - %(message)s',
            level=level,
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    logger = logging.getLogger()
    logger.debug('Entering main')
    latest_info = get_latest_info()

    class BaseValues(Enum):
        # base date and base time are
        # per the retirement site
        base_date = latest_info['date']
        base_time = latest_info['value']
        max_time = 30

    logger.debug(BaseValues.base_date.value)
    logger.debug(BaseValues.base_time.value)

    base_date_obj = datetime.strptime(BaseValues.base_date.value, "%Y-%m-%d")
    today = datetime.today()
    logger.debug(f'base date: {base_date_obj}')
    logger.debug(f'today: {today}')
    logger.debug(f'days diff: {(today - base_date_obj).days}')
    days_elapsed = (today - base_date_obj).days
    fraction_of_a_year = round(days_elapsed / 365, 5)
    logger.debug(f'fraction_of_a_year: {fraction_of_a_year}')

    # BASE_TIME_SERVED needs to be incremented by the
    # number of days elapsed since the BASE_DATE
    logger.debug(f'base time served - from web site: {BaseValues.base_time.value}')
    adjusted_base_time = float(BaseValues.base_time.value) + fraction_of_a_year
    logger.debug(f'base time served - plus days elapsed:  {adjusted_base_time}')

    # max out at 30 years
    time_to_max = round(BaseValues.max_time.value - adjusted_base_time, 5)
    logger.debug(f'time to max: {time_to_max}')
    # time_to_max is a floating point
    # need to get the actual number of total days
    # out of it
    #
    # break down the time left into components
    frac, whole = math.modf(time_to_max)
    logger.debug(f'frac: {round(frac, 5)} .. whole: {whole}')
    years_to_max = int(whole)
    logger.debug(f'years to max: {years_to_max}')
    days_to_max = round(frac * 365)
    logger.debug(f'days to max: {days_to_max}')
    # round this figure
    days_to_max = math.ceil(days_to_max)
    ttl_days_left = (years_to_max * 365) + days_to_max + 1
    logger.debug(f'ttl days left: {ttl_days_left}')
    end_date = today + timedelta(days=ttl_days_left)
    today = datetime.today()
    print(f'\n  Today is: \t\t\t{today.strftime("%m/%d/%Y")}')
    print(f'  Retirement maxes out: \t{end_date.strftime("%m/%d/%Y")}\n')

    days_left = (end_date - today).days
    years_left = int(days_left / 365)
    days_left = days_left - (years_left * 365)

    # print(f'\n{years_left} years and {days_left} days left\n')

    diff = relativedelta.relativedelta(end_date, today)
    years = diff.years
    months = diff.months
    days = diff.days + 1

    outputstr = construct_output_string(years, months, days)

    # print(f'years: {years} -- months: {months} -- days: {days}')
    # outputstr = ''
    #
    # if years > 1:
    #     outputstr = outputstr + f'{years} years '
    # elif years == 1:
    #     outputstr = outputstr + f'{years} year '
    #
    # if months and years:
    #     outputstr = outputstr + f', '
    #
    # if months > 1:
    #     outputstr = outputstr + f'{months} months '
    # elif months == 1:
    #     outputstr = outputstr + f'{months} month '
    #
    # if days:
    #     outputstr = outputstr + f'and '
    #
    # if days > 1:
    #     outputstr = outputstr + f'{days} days '
    # elif days == 1:
    #     outputstr = outputstr + f'{days} day '
    #
    # outputstr = outputstr + f'left'

    print(f'  {outputstr}\n\n')


if __name__ == '__main__':
    main()
