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

def compare(u_score, c_score):
    if c_score == 0:
        return -1
    elif u_score == 0:
        return 1
    elif u_score > 21:
        return -1
    elif c_score > 21:
        return 1
    elif u_score > c_score:
        return 1
    elif u_score < c_score:
        return -1
    else:
        return 0

playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while playing == 'y':
    print(art.logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card)
        computer_cards.append(deal_card)
    drawing = 'y'
    game_over = False
    while drawing == 'y':
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your hand is: {user_cards}, with a score of {user_score}.")
        print(f"The computer's first card is {computer_cards[0]}.")
        if computer_score == 0:
            print(f"The computer's hand is {computer_cards}, with a score of {computer_score}, a blackjack.")
            print("You lose!")
            drawing = 'n'
            game_over = True
        elif user_score == 0:
            print("You have a blackjack! You win!")
            drawing = 'n'
            game_over = True
        elif user_score > 21:
            print("Your score is over 21. You lose!")
            drawing = 'n'
            game_over = True
        else:
            drawing = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            if drawing == 'y':
                user_cards.append(deal_card)
    if not game_over:
        while computer_score < 16:
            computer_cards.append(deal_card)
            computer_score = calculate_score(computer_cards)
        game_state = compare(user_score, computer_score)
        print(f"Your hand is: {user_cards}, with a score of {user_score}.")
        print(f"The hand of the computer is: {computer_cards}, with a score of {computer_score}.")
        if game_state == 1:
            print("You win!")
        elif game_state == -1:
            print("You lose!")
        else:
            print("It's a draw!")
    playing = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    
print("Thank you for playing?")