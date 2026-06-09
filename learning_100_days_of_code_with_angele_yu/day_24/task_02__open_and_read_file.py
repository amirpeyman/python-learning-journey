# Open and Read Files 👇

# =======================
# Read file - Method 1
# =======================
file = open("my_file_1.txt")    # After this line, if we run the program, nothing appears to happen,
                                # but behind the scenes, Python has opened the file and is ready for the next action.❗
contents = file.read()
print(contents)
file.close()                    # When a file is opened, system resources are allocated to it.
                                # Manually closing the file frees those resources. But we might forget to do so ⚠️


# =======================
# Read file - Method 2 👍
# =======================
# To solve the problem of forgetting to close the file, we open the file as follows 👇

with open("my_file_1.txt") as file:     # 'file' is basically equivalent to 'my_file_1.txt' ✅
    contents = file.read()
    print(contents)
    # file.close()                      # We no longer need to close the file manually 👍
