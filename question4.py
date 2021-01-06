""" Sorting the dictionary using lambda """

dict_list = [
    {"make": "Nokia", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": 2, "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]
# Using lambda to sort the dictionary
sorted_list = sorted(dict_list, key=lambda key: key["model"], reverse=True)
print(sorted_list)
