# Banker Roulette practice 👇
import random

# Solution 1️⃣
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))

# Solution 2️⃣
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_index = random.randint(0, 4)
print(friends[random_index])
