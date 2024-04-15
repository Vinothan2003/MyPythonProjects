import json
from pathlib import Path

details = [
    {"ID": 2002141, "Name": "Vinothan NC", "Age": 20}, {"ID": 2002111, "Name": "hello123", "Age": 20}
]

# writing data into json file
data = json.dumps(details)
# print(data)

# Path("details_data.json").write_text(data)

# reading the data from json file
read_data = Path("details_data.json").read_text()
details_data = json.loads(read_data)
print(details_data)
