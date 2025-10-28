# Simple functions without inputs 👇
def greet():
    print("Hello")
    print("How do yo do?")
    print("Isn't the weather nice?")

greet()

# Functions that allows for inputs 👇
def greet_with_name(name):                          # name ==> is Parameter ✅
    print(f"Hello {name}")
    print(f"How do yo do {name}?")
    print(f"Isn't the weather nice?")

greet_with_name("Peyman")                           # Peyman ==> is Argument ✅
greet_with_name("Amir")


# "Life in Weeks" practice 👇
def life_in_weeks(age):
    year_remaining = 90 - age
    weeks_remaining = year_remaining * 52
    print(f"You have {weeks_remaining} weeks left.")

your_age = int(input("How old are you? "))
life_in_weeks(your_age)
