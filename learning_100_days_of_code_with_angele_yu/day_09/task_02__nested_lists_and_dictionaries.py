# Nested Lists and Nested Dictionaries 👇

# Very simple dictionary 👇
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
print(capitals)
print("\n")

# Nested list in dictionary 👇
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],    # "France": "Paris", "Lille", "Dijon" ❌ Each key can only have one value
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log)
print("\n")

# PAUSE 1 ==> How to print out "Lille" from travel_log dictionary 👇
print(travel_log["France"][1])
print("\n")

# Nesting Lists inside other Lists 👇
nested_list = ["A", "B", ["C", "D"]]
print(nested_list)
print("\n")

# Get items that are nested deeply in a list ==> Print item 'D' 👇
print(nested_list[2][1])
print("\n")

# Nesting a Dictionary inside a Dictionary 👇
travel_log = {
    "France": {
        "num_times-visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visited": 5,
    },
}
print(travel_log)
print("\n")

# Get items that are nested deeply in a dictionary ==> Print item "Stuttgart" 👇
print(travel_log["Germany"]["cities_visited"][2])
