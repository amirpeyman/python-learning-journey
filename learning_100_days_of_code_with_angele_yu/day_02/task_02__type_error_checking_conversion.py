# Type Error 👇
# len(12345) #❌
len("12345") #✅

# Variable Type Checking with type() function 👇
print(type("Hello"))
print(type(12345))
print(type(-123))
print(type(3.14159))
print(type(True))

# Type Casting ==> Conversion Data Types to each other 👇
print("123" + "456")
print(int("123") + int("456"))      # Type Casting done ✅
print(float(456))                   # Type Casting done ✅
print(str(123) + str(789))          # Type Casting done ✅

# Value Error 👇
# print(int("abc"))                 # Type Casting not done ==> Value Error ❌

# PAUSE 3 ==> '+' can only concatenate str to str 👇
name_of_the_user = input("Enter your name: ")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: ")) # str
print(type(length_of_name))                     # int

print("Number of letters in your name: " + str(length_of_name))
