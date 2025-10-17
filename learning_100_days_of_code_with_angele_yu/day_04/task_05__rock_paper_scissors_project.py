# Rock Paper Scissors Project 👇
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
wrps = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if 0 <= user_choice <= 2:
    print(wrps[user_choice])
else:
    print("Your input is wrong! ❌\n")

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{wrps[computer_choice]}")

# Solution 1️⃣ (Myself)
if 0 <= user_choice <= 2:
    if user_choice == 0 and computer_choice == 2:
        print("You Win 😊")
    elif user_choice == 2 and computer_choice == 1:
        print("You Win 😊")
    elif user_choice == 1 and computer_choice == 0:
        print("You Win 😊")
    elif user_choice == computer_choice:
        print("It's a draw")
    else:
        print("You Lose 😭")
else:
    print("Please try again")


# Solution 2️⃣ (Teacher)
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw!")
