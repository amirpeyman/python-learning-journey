# Simple functions 👇
def greet():
    print("Hello")
    print("How do yo do?")
    print("Isn't the weather nice?")


greet()
print("\n")


# Functions that allows for inputs 👇
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do yo do {name}?")
    print(f"Isn't the weather nice?")


greet_with_name("Peyman")
greet_with_name("Amir")
print("\n")


# Functions that return output 👇
def my_function():
    result = 3 * 2
    return result   # After the 'return' keyword, specify the value that will be used as the function’s output ✅


output = my_function()
print(output)
print("\n")


# Example 👇
output = len("Amirpeyman")  # The len() function takes a string as input and returns a number as its output ✅
print(output)
print("\n")


# PAUSE 1 & 2 - Title Case 👇
def format_name(f_name, l_name):
    formated_f_name = f_name.title()    # You can use the title() function to convert any string to title case ✅
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


# formated_string = format_name("amIrPeYmAn", "nAHnaEI")
# print(formated_string)
print(format_name("amIrPeYmAn", "nAHnaEI"))
print("\n")


# Using the output of one function as the input for another function 👇
def function_1(text):
    return text + text

def function_2(text):
    return text.title()


output = function_2(function_1("hello"))    # ✅
print(output)
