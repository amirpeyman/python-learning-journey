# Multiple Return Values 👇

# The line containing the 'return' statement marks the end of the function.
# The function is considered 'terminated' at this point, and any code after it will not be executed 👇
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"           # You can also use Empty Return ❗
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"   # ✅
    print("This got printed")                               # ❌


print(format_name(input("What is your first name? "), input("What is your last name? ")))


# Leap Year Project 👇
def leap_year_checker(year_number):
    if year_number % 4 == 0:
        if year_number % 100 == 0:
            if year_number % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
    else:
        return "Not Leap"


year = int(input("Enter year number? "))
print(leap_year_checker(year))
