# Index Error ==> When try to access an item that is not in the range of the List 👇
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Tim", "Montana", "Washington", "Idaho", "Wyoming", "Utah",
                     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(len(states_of_america))
# print(states_of_america[50])      # ❌ This will be an IndexError
print(states_of_america[49])        # ✅

# Fix Index Error Solution 👇
num_of_states = len(states_of_america)         # 50 -> 49
print(states_of_america[num_of_states - 1])    # ✅


# Nested Lists (2D List)👇
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes",
#                "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]              # ❌

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]                                                              # ✅ Nested Lists
print(dirty_dozen)

print(dirty_dozen[0][2])
