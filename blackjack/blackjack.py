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
    return score

playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while playing == 'y':
    print(art.logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card)
        computer_cards.append(deal_card)
    