import json

with open("ret.json") as jsn:
    data = json.load(jsn)

print(type(data))
print(data)
for i in data:
    print(f'{type(i)} -- {i}')
    print(f'{i["date"]}')

add_date = input('Date: ')
add_value = input('Value: ')
add_dict = {"date": add_date, "value": add_value}
print(f'{add_dict}')
print(f'=================================')
data.append(add_dict)
print(data)
print(f'=================================')

with open("ret.json", "w") as jsn:
    json.dump(data, jsn)