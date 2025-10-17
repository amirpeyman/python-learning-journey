# Randomisation 👇

# To use "Random Module in Python" you need to first import it 👇
import random
# Python use "Mersenne Twister Algorithm" ==> The Mersenne Twister is a popular pseudo random number generator (PRNG)✅
random_integer = random.randint(1, 9)   # Random whole numbers within a range✅
print(random_integer)

# Here I imported my module that I had already written in the my_module.py file 👇
import my_module
print(my_module.my_favorite_number)           # my_favorite_number is a variable that defined in the my_module.py file✅

# Generate Random Floats 👇
random_number_0_to_1 = random.random()        # Some functions can be empty (without input) e.g. random()✅
print(random_number_0_to_1)

random_number_0_to_10 = random.random() * 10
print(random_number_0_to_10)

random_float = random.uniform(0, 1)     # If you want the upper bound included✅
print(random_float)

# `random.random()` returns a random number between 0 and 1
# while `random.uniform(a, b)` returns a random number between any two given values `a` and `b`.

# PAUSE 1 - Heads or Tails 👇
random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
