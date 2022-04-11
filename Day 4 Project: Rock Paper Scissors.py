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

#Write your code below this line 👇

game_images = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

computer_choice = random.randint(0,2)

if user_choice > 2 or user_choice < 0:
  print("Invalid. You lose.")
else:
  print(game_images[user_choice])
  print(f"Computer chose {computer_choice}")
  print(game_images[computer_choice])
  if user_choice == computer_choice:
    print("It's a draw. Try again.")
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif user_choice == 2 and computer_choice == 0:
    print("You lose")
  elif computer_choice > user_choice:
    print("You lose")
  elif user_choice > computer_choice:
    print("You win!")
  else:
    print("Invalid, you lose")
