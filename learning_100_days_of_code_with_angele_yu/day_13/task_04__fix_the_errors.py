# Fix the Errors 👇

# Fix 'red underlines' ❌ and check 'yellow underlines' ⚠️
# age = int(input("How old are you? "))
# if age > 18:
# print("You can drive at age {age}.")



# Catching Exceptions ==> Use 'try/except block' 👇
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response as 15.")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")
