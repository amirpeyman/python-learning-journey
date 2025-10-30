# Python Dictionaries 👇

# Standard convention for writing dictionaries by Python programmers 👇
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
print(programming_dictionary)
print("\n")

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
}
print(colours)
print("\n")

# Retrieve items (or fetch data) from a dictionary 👇
print(programming_dictionary["Bug"])
print(colours["pear"])
print("\n")

# Create an empty dictionary 👇
my_empty_dictionary = {}
print(my_empty_dictionary)
my_empty_dictionary["Example"] = "Peyman"
print(my_empty_dictionary)
print("\n")

# Add new items to an existing dictionary 👇
programming_dictionary["If"] = "A fundamental control flow statement"
print(programming_dictionary)

colours["Blueberries"] = "blue"
print(colours)
print("\n")

# Edit an existing value in a dictionary 👇
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

colours["apple"] = "pink"
print(colours)
print("\n")

# Delete items from an existing dictionary 👇
del programming_dictionary["Bug"]
print(programming_dictionary)

del colours["apple"]
print(colours)
print("\n")

# Wipe an entire dictionary 👇
programming_dictionary = {}
print(programming_dictionary)

colours = {}
print(colours)
print("\n")

# Loop through a dictionary and print all the keys and all the values 👇
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
for thing in programming_dictionary:
    print(thing)                            # Print all keys 🔑
    print(programming_dictionary[thing])    # Print all values 🥣

print("\n")

colours = {
    "apple": "red",
    "pear": "green",
    "banana": "yellow",
}
for key in colours:
    print(key)                              # Print all keys 🔑
    print(colours[key])                     # Print all values 🥣

print("\n************************")

# Grading Program Practice 👇
student_score = {
    "Harry": 88,
    "Ron": 78,
    "Hermione": 95,
    "Draco": 75,
    "Neville": 60,
}

student_grades = {}

for student in student_score:
    score = student_score[student]

    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print("Student Grading Program\n")
for student in student_grades:
    print(f"{student} should have grade {student_grades[student]}")
