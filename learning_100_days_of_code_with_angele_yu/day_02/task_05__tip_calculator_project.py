# Tip Calculator Project 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
bill_per_person = bill / people * (1 + tip / 100)
print(f"Each person should pay: ${round(bill_per_person, 2)}")
