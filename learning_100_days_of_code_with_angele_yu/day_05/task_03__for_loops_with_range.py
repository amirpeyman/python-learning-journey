# For Loops with Range() - to run a loop for as many times as we wish 👇

for number in range(1, 11):     # for 1 to 10
    print(number)


for number in range(1, 11, 3):  # increase by 3
    print(number)



# PAUSE 1 - The Gauss Challenge ==> total of the numbers between 1 and 100 👇
total = 0
for number in range(1, 101):
    total += number
print(total)



# FizzBuzz Game 👇
print("Welcome to FizzBuzz game")
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
