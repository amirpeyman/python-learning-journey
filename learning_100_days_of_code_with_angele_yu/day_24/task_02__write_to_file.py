# Write to Files 👇

with open("my_file_2.txt", mode="a") as file:   # The default value of the mode argument is 'r', which stands for 'read'.
                                                # For writing, we use 'w', and for appending, we use 'a'.
    file.write("\nNew text.")


with open("new_file.txt", mode="w") as file:    # In this case, the file 'new_file.txt' is created automatically ✅
    file.write("New text.")
