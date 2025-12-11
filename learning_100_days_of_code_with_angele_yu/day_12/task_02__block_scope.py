# Python does not have block scope 👇❗

# Blocks of code e.g. for loops, if statements, while loops etc. do not create a local scope ❗
if 3 > 2:
    a_variable = 10

print(a_variable)




game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)        # new_enemy is accessible because 'if' does not create a local scope ✅




# def create_enemy():
#     game_level = 10
#     enemies = ["Skeleton", "Zombie", "Alien"]
#
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
#
# print(new_enemy)  # new_enemy isn't accessible because the create_enemy() function has created a local scope ❌




# Prime Number Checker Example 👇
def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(7))
