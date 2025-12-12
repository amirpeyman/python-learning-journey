# Use Print for Debugging 👇

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)




# Print is your friend ==>  It can help expose hidden values while your code is running 👇
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page

print(f"pages = {pages}")                       #✅
print(f"world_per_page = {word_per_page}")      #✅
print(total_words)
