import math
from datetime import datetime
from datetime import timedelta

# per the retirement site
BASE_DATE = '2018-06-02'
base_date_obj = datetime.strptime(BASE_DATE, "%Y-%m-%d")

# per the retirement site
BASE_TIME_SERVED = 27.78206

# max out at 30 years
TIME_TO_MAX = 30 - BASE_TIME_SERVED

# time_to_max is a floating point
# need to get the actual number of total days
# out of it
#
# break down the time left into components
frac, whole = math.modf(TIME_TO_MAX)
years_to_max = int(whole)
days_to_max = frac * 365

# round this figure
days_to_max = math.ceil(days_to_max)
ttl_days_left = (years_to_max * 365) + days_to_max

end_date = base_date_obj + timedelta(days=ttl_days_left)
today = datetime.today()
print(f'\ntoday is: \t\t{today.strftime("%m/%d/%Y")}')
print(f'projected end date: \t{end_date.strftime("%m/%d/%Y")}')

days_left = (end_date - today).days
years_left = int(days_left / 365)
days_left = days_left - (years_left * 365)

print(f'\n{years_left} years and {days_left} days left\n')
