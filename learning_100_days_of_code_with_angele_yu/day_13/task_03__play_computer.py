# Playing computer is an important skill in debugging 👇

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


"""
year = 1994
year > 1980 ==> True
year < 1994 ==> False
True and False ==> False ❌

year > 1994 ==> False ❌
"""


if False:
    print("You are a millennial.")
elif False:
    print("You are a Gen Z.")


# Solve Problem 👇
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994: #✅
    print("You are a Gen Z.")

# Or 👇
if year > 1980 and year <= 1994: #✅
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")
