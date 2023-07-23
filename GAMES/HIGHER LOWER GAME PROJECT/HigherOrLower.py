import random
import art
import GameData
from replit import clear

A = random.choice(GameData.data)
B = random.choice(GameData.data)
score = 0


def compare(F1, F2):
    if F1['follower_count'] > F2['follower_count']:
        return "A"
    return "B"


game = True

while game:
    print(art.logo)
    if score > 0:
        print(f"You're right! Current Score:{score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

    lead = compare(A, B)
    Guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    if lead == Guess and Guess == "A":
        score += 1
        B = random.choice(GameData.data)
    elif lead == Guess and Guess == "B":
        score += 1
        A = B
        B = random.choice(GameData.data)
    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final score {score}")
        game = False

