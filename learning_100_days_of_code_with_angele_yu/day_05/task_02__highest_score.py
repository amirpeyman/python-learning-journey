# Highest Score practice 👇
# Solution 1️⃣ ==> using the sum() function
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)
print(total_score)

# Solution 2️⃣ ==> using a for loop
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = 0
for score in student_scores:
    total_score += score
print(total_score)


# PAUSE 1 - Max & Min 👇

# Max solution 1️⃣ ==> using the max() function
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(max(student_scores))

# Max solution 2️⃣ ==> using a for loop
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)



# Min solution 1️⃣ ==> using the min() function
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(min(student_scores))

# Min solution 2️⃣ ==> Using a for loop
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
min_score = student_scores[0]
for score in student_scores:
    if score < min_score:
        min_score = score
print(min_score)

# Min solution 3️⃣ ==> Using float('inf')
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
min_score = float('inf')    # The concept of float('inf') in Python is to represent a number
                            # that is much larger than any other numeric value and means "positive infinity"
                            # 'inf' stands for "infinity"
for score in student_scores:
    if score < min_score:
        min_score = score
print(min_score)
