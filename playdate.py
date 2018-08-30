import math
from datetime import datetime
from datetime import timedelta
from dateutil import relativedelta
from enum import Enum
import logging
import sys


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

    # base date and base time are
    # per the retirement site
    class BaseValues(Enum):
        base_date = '2018-12-31'
        base_time = 27.92007
        max_time = 30

    # 27.78206
    # 6 / 2 / 18
    #
    # 6 / 30
    # 27.92007
    #
    # base_date = '2018-06-16'
    # base_time = 27.87407

    logger.debug(BaseValues.base_date.value)
    logger.debug(BaseValues.base_time.value)

    base_date_obj = datetime.strptime(BaseValues.base_date.value, "%Y-%m-%d")
    today = datetime.strptime('2018-12-31', "%Y-%m-%d")

    diff = relativedelta.relativedelta(base_date_obj, today)
    years = diff.years
    months = diff.months
    days = diff.days + 1

    print(f'years: {years} -- months: {months} -- days: {days}')
    outputstr = ''

    if years > 1:
        outputstr = outputstr + f'{years} years'
    elif years == 1:
        outputstr = outputstr + f'{years} year'

    if months and years:
        outputstr = outputstr + f', '

    if months > 1:
        outputstr = outputstr + f'{months} months'
    elif months == 1:
        outputstr = outputstr + f'{months} month'

    if days and months and years:
        outputstr = outputstr + f', and '
    elif days and months:
        outputstr = outputstr + f' and '

    if days > 1:
        outputstr = outputstr + f'{days} days '
    elif days == 1:
        outputstr = outputstr + f'{days} day '

    outputstr = outputstr + f'left'

    print(f'output str: {outputstr}')


if __name__ == '__main__':
    main()
