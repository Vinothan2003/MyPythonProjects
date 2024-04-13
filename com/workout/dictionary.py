"""worker = {
    "name": "Vinothan NC",
    "age": 20,
    "birthdate": "06/09/2003",
    "phone_no": 8778786481
}
print(worker["name"])
# print(worker["Name"])

print(worker.get("Name"))
print(worker.get("name"))"""

people = {1: {'Name': 'John', 'Age': 27, 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': 22, 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
