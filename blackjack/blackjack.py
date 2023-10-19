import art
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    score = 0
    for card in card_list:
        score += card
        if card == 11 and score > 21:
            score -= 10
            card_list.remove(card)
            card_list.append(1)
    if score == 21:
        score = 0
    return score

playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while playing == 'y':
    print(art.logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card)
        computer_cards.append(deal_card)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your hand is: {user_cards}, with a score of {user_score}.")
    if computer_score == 0:
        print(f"The computer's hand is {computer_cards}, with a score of {computer_score}, a blackjack.")
        print("You lose!")
    elif user_score == 0:
        print("You have a blackjack! You win!")
    elif user_score > 21:
        print("Your score is over 21. You lose!")