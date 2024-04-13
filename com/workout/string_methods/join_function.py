myDict = {"name": "John", "country": "Norway"}
mySeparator = ","

# x = ','.join([value for value in myDict.values()])

value_list = []
for keys, values in myDict.items():
    value_list.append(values)

x = mySeparator.join(value_list)
print(x)