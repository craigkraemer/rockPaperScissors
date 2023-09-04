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

#Write your code below this line 👇

import random

player = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors?\n")

player = int(player)

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
elif player == 2:
    print(scissors)
else:
    print("You typed an incorrect number.")


computer = random.randint(0, 2)

if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
else:
    print("The computer entered an incorrect number.")


if player == computer:
    print("It's a draw.")
elif player == 0 & computer == 1:
    print("Computer wins.")
elif player == 0 & computer == 2:
    print("Player wins.")
elif player == 1 & computer == 0:
    print("Player wins.")
elif player == 1 & computer == 2:
    print("Computer wins.")
elif player == 2 & computer == 0:
    print("Computer wins.")
elif player == 2 & computer == 1:
    print("Player wins.")
else:
    print("Unknown Error.")