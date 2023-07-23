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

# Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp = random.randint(0, 2)
game_img = [rock, paper, scissors]
print(game_img[choice])

print("\nComputer chose:")
print(game_img[comp])

if (choice == 0 and comp == 1) or (choice == 1 and comp == 2) or (choice == 2 and comp == 0) or (
        choice == 0 and comp == 2):
    print("\nYou lose")
elif (comp == 0 and choice == 1) or (comp == 1 and choice == 2) or (comp == 2 and choice == 0) or (
        comp == 0 and choice == 2):
    print("\nYou win ")
else:
    print("\nDraw")
