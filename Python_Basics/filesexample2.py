import simplejson as json  # gives an alias to the import
import os

# if file exists opens the file and updates the age one year
if os.path.isfile("./example.json") and os.stat("./example.json").st_size != 0:
    example_file = open("example.json", "r+")
    data = json.loads(example_file.read())
    print("Current age is", data["age"], "-- adding a year.")
    data["age"] += 1
    print("New age is", data["age"])
else:
    # if it doesn't exist create a new file with the data information
    example_file = open("example.json", "w+")
    data = {"name": "João", "age": 31,
            "city": "Lisbon", "nacionality": "portuguese"}
    print("No file found, setting default age to", data["age"])

example_file.seek(0)
# example_file.write(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
example_file.write(json.dumps(data, indent=4))
