""" Program to convert key sorted Python dictionary to JSON """
import json

# Hard coding the dictionary.
dictionary = {"make": "Nokia", "model": 216, "color": "Black"}, {
    "make": "Mi Max",
    "model": "2",
    "color": "Gold",
}
json = json.dumps(dictionary, indent=4, sort_keys=True)
print(json)
