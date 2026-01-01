# Use Python Packages 👇

# First, we install the package, and then we use it 👇
from prettytable import PrettyTable

table = PrettyTable()                                                                       # Create object ✅

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])     # Calling method ✅
table.add_column("Type", ["Electric", "Water", "Fire"])                     # Calling method ✅
table.align = "l"                                                                           # Tap attribute ✅

print(table)
