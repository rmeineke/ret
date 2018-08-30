import json

with open("ret.json") as jsn:
    data = json.load(jsn)

# latest_date = '';
# latest_value = ''
# for i in data:
#     latest_date = i['date']
#     latest_value = i['value']
#
# print(f'{latest_date}')
# print(f'{latest_value}')
print(f'{type(data)}')
print (data[-1])