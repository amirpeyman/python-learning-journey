# Reproduce the Bug 👇

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])


# Test with dice_num = 1 ✅
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 1
print(dice_images[dice_num])

# Test with dice_num = 2 ✅
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 2
print(dice_images[dice_num])

# Test with dice_num = 3 ✅
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 3
print(dice_images[dice_num])

# Test with dice_num = 4 ✅
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 4
print(dice_images[dice_num])

# Test with dice_num = 5 ✅
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 5
print(dice_images[dice_num])

# Test with dice_num = 6 ❌
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = 6
print(dice_images[dice_num])


"""
As a result:
dice_num = 1✅
dice_num = 2✅
dice_num = 3✅
dice_num = 4✅
dice_num = 5✅
dice_num = 6❌
So: 👇
"""
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_images[dice_num])
