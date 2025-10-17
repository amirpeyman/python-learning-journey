# Python Lists (or Data Structure) ==> For organizing and storing collection of ordered items 👇
# Syntax ==> list_of_variables = [item1, item2, item3]
fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america)
print(states_of_america[2])

# Negative Indices 👇
print(states_of_america[-1])

# Modifying Items 👇
states_of_america[1] = "Pencilvania"
print(states_of_america)

# Adding Items (only single item at the end of list) 👇
fruits.append("Tangerine")
print(fruits)

# Adding multiple items 👇
fruits.extend(["Orange", "Berry"])
print(fruits)
