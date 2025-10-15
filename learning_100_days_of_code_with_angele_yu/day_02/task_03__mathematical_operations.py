# Mathematical Operations

print(123 + 456)    # Addition
print(7 - 3)        # Subtraction
print(3 * 2)        # Multiplication
# Implicit typecasting (Default Python behavior at the time of division) 👇
print(5 / 3)        # Division with float result
print(type(6 / 2))
# Fix implicit typecasting 👇
print(5 // 3)       # Division with int result
print(type(6 // 3))
print(2 ** 3)       # Exponents

# PEMDAS ==> Parentheses, Exponents, Multiplication/Division, Addition/Subtraction 👇
# 1️⃣() 2️⃣** 3️⃣* OR / 4️⃣+ OR -
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) // 3 - 3)

# BMI Practice 👇
# Formula = Weight / Height ** 2
print("BMI Calculator")
weight = float(input("Your weight? "))
height = float(input("Your height? "))
bmi = weight / height ** 2
print("Your BMI is: " + str(bmi))
