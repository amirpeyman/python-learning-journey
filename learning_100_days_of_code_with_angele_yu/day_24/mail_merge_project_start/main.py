# Mail Merge Project 👇

PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    # readlines() Method ==> Return all lines in the file, as a list where each line is an item in the list object ✅
    names = names_file.readlines()

with open("./input/letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # String strip() Method ==> Removes any leading, and trailing whitespaces ✅
        stripped_name = name.strip()
        # String replace() Method ==> Replaces a specified phrase with another specified phrase ✅
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ready_to_send/letter_for_{stripped_name}.doc", mode="w") as completed_letter:
            completed_letter.write(new_letter)
