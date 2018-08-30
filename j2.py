import json

with open('csj2017.v2.json', encoding='utf-8') as jsn:
    data = json.load(jsn)
#
# print(type(data))
# print(data)
#
# print(len(data))

for item in data:
    print(item[0])
    print(item[1])
    print(item[2])
    print(item[3])