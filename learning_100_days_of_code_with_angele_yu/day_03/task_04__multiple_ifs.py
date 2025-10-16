# Multiple Ifs ==> To check for different conditions that are unrelated to each other 👇
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age?\n"))
    if age <= 12:                                   # Condition 1: Age🅰️
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")
    if wants_photo == "y":                          # Condition 2: Photo🅱️
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you can't ride.")
