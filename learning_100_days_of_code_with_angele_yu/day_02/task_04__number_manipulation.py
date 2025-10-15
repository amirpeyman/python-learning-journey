bmi = 84 / 1.65 ** 2
print(bmi)              # 30.85399449035813✅

# Flooring a number with int() function 👇
print(int(bmi))         # 30✅

# Rounding a number with round() function 👇
print(round(bmi))       # 31✅

# Rounding a number with round() function and n'digits value 👇
print(round(bmi, 2))    # 30.85✅


# Assignment Operators ==> += , -= , *= , /= , //=
score = 5
# score = score + 3 # ❌
score += 3          # ✅
print(score)


# f-Strings method ==> To insert a variable or an expression into a string 👇
age = 12
is_winning = True
print("I am " + str(age) + " years old. You are winning is " + str(is_winning) + ".")   # without f-string❌
print(f"I am {age} years old. You are winning is {is_winning}.")                        # with f-string✅
