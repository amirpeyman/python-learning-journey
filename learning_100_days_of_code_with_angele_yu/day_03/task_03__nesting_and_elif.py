# Nesting ==> Nested If/Else Condition Statements 👇
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5")
    # elif ==> elif instead of else when there are more than 2 possibilities 👇
    # else:
    #     print("Please pay $7")
    elif age <= 18:
        print("please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you can't ride.")


# BMI Practice 👇
# Formula = Weight / height ** 2
print("BMI Calculator")
weight = float(input("Your weight? "))
height = float(input("Your height? "))
bmi = weight / height ** 2
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
else:
    print("Overweight")
