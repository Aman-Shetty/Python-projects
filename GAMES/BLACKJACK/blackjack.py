import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def blackjack(card):
    if add(card) == 21:
        return True
    return False


def compare(user, comp, user_sum, comp_sum):
    if comp or (comp and user) or user_sum > 21:
        print("You lose")
        print(f"USER : {user_sum}")
        print(f"COMPUTER : {comp_sum}")
        play_again()
    elif user or comp_sum > 21:
        print("You Win!!")
        print(f"USER : {user_sum}")
        print(f"COMPUTER : {comp_sum}")
        play_again()
    elif 16 < comp_sum == user_sum > 16:
        print("Draw!!")
        print(f"USER : {user_sum}")
        print(f"COMPUTER : {comp_sum}")
        play_again()
    elif (comp_sum > user_sum) and comp_sum > 16:
        print("You lose")
        print(f"USER : {user_sum}")
        print(f"COMPUTER : {comp_sum}")
        play_again()
    elif (comp_sum < user_sum) and comp_sum > 16:
        print("You Win!!")
        print(f"USER : {user_sum}")
        print(f"COMPUTER : {comp_sum}")
        play_again()


def play_again():
    again = input("Do you want to play again?: Y/N ").upper()
    if again == "N":
        exit()
    elif again == "Y":
        play()


def add(card):
    add = 0
    for pick in card:
        if add + pick > 21 and pick == 11:
            add = add + 1
        else:
            add = add + pick

    return add


def play():
    print(logo)
    print("\n")
    user_cards = []
    computer_cards = []

    for i in range(0, 2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"Your cards : {user_cards} \t Your score: {add(user_cards)}")
    print(f"Computer's cards : {computer_cards[0]} ")

    user = blackjack(user_cards)
    comp = blackjack(computer_cards)
    user_sum = add(user_cards)
    comp_sum = add(computer_cards)
    compare(user, comp, user_sum, comp_sum)

    next_move = "draw"
    while user_sum < 17 and next_move == "draw":
        next_move = input("Do you want to 'draw' or 'stand'?: ").lower()
        if next_move == "draw":
            user_cards.append(deal_card())
            print(f"Your cards : {user_cards} \t Your score: {add(user_cards)}")
            print(f"Computer's cards : {computer_cards[0]} ")
            user_sum = add(user_cards)
            compare(user, comp, user_sum, comp_sum)
        else:
            compare(user, comp, user_sum, comp_sum)
            print(f"Your cards : {user_cards} \t Your score: {add(user_cards)}")
            print(f"Computer's cards : {computer_cards} ")

    while comp_sum < 17:
        computer_cards.append(deal_card())
        comp_sum = add(computer_cards)
        compare(user, comp, user_sum, comp_sum)


play()
