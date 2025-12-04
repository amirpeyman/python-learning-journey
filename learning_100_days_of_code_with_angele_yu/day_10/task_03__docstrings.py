# DocStrings 👇

def format_name(f_name, l_name):
    """
    Take a first and last name and format it to 
    return the title case version of name.
    """                                                             # DocString ✅
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("aMIrPeYmaN", "nAhnAEi")
print(formatted_name)
print("\n")



def leap_year_checker(year_number):
    """
    Returns "Leap" if year is a leap year, otherwise "Not Leap".
    """                                                             # DocString ✅
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
print("\n")



# Nested Function Example 👇
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)
