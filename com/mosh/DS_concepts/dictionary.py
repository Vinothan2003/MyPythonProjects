# Dictionary --> store the data in key value pairs
details = {
    "name": "Vinothan NC",
    "age": 20,
    "phone": 8778786481
}
print(details)
print(details["name"])
print(details.get("Age"))  # case sensitive

details_2 = dict(name="Tamil Kadavul", age=100000, phone="tamil ku en 1 Aluthavum")  # another way of creating a dictionary
print(details_2)

print(details_2.get("name"))
print(details_2.get("DOB", "unknown"))

details_2.update(address="mela par kulathai")
print(details_2.keys())
print(details_2.values())
print(details_2)

details_2.pop("address")
print(details_2)

for key, value in details_2.items():  # unpacking key: key | value : value
    print(key, value)

for key in details:
    print(key,  details[key])  


