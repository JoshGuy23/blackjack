import art
import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while playing == 'y':
    print(art.logo)