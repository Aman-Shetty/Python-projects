import random
import HangmanWords
import HangmanArt


print("\n")
print(HangmanArt.logo)

chosen_word = random.choice(HangmanWords.word_list)

word = []
display = ""
for i in range(0, len(chosen_word)):
    word.append("_")
for letter in word:
    display = display + letter
print(display)

end = False
life = 5

while not end:
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print(f"You have already chosen letter {guess}")

    index = 0
    for letter in chosen_word:
        if letter == guess:
            word[index] = letter
        index += 1

    if (guess not in chosen_word) and (guess not in word):
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        life -= 1
        if life == 0:
            print(f"The word is {chosen_word}, You lose!!")
            end = True

    display = ""
    for letter in word:
        display = display + letter

    print(display)
    if "_" not in word:
        end = True
        print("You Win!!")

    print(HangmanArt.stages[life])
