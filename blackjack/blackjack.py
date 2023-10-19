import art                      # Import ASCII art for logo
import random                   # Import random module for random dealing of cards
import os                       # Import os module for clearing the screen.

# This function takes a list of values (not cards) that are usually present in blackjack, and randomly returns one of them.
# The function returns random.choice(cards), a random selection from the list of cards.
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# This function calculates a player's score from their hand.
# card_list is a list representation of a player's hand.
# A blackjack is returned as a 0.
# If an 11 is in the player's hand and their score is over 21, replace that card with a 1 and change the score to reflect that.
def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score > 21:
        score -= 10
        card_list.remove(11)
        card_list.append(1)
    if score == 21:
        score = 0
    return score

# This function compares the scores of the user and computer to see who won blackjack.
# u_score is the user's score, and c_score is the computer's score.
# If the player wins, 1 is returned. For the computer, -1. For a draw, 0.
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

# Ask whether the player wants to play blackjack.
playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# Keep playing blackjack as long as the user wants to.
while playing == 'y':
    # Display the ASCII logo.
    print(art.logo)
    # Prepare the hands for each player.
    user_cards = []
    computer_cards = []
    # Deal 2 cards to each player's hand.
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    drawing = 'y'
    game_over = False
    # Continue drawing until either a game over or the user passes.
    while drawing == 'y':
        # Calculate the scores of the user and the computer.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        # Display the user's hand and score as well as the first card of the computer's hand.
        print(f"Your hand is: {user_cards}, with a score of {user_score}.")
        print(f"The computer's first card is {computer_cards[0]}.")
        if computer_score == 0: # The computer wins if they scored a blackjack.
            print(f"The computer's hand is {computer_cards}, with a score of {computer_score}, a blackjack.")
            print("You lose!")
            drawing = 'n'
            game_over = True
        elif user_score == 0:   # Otherwise, if the user gets a blackjack, they win.
            print("You have a blackjack! You win!")
            drawing = 'n'
            game_over = True
        elif user_score > 21:   # Otherwise, if the user's score is over 21, they lose.
            print("Your score is over 21. You lose!")
            drawing = 'n'
            game_over = True
        else:                   # Otherwise, continue drawing.
            drawing = input("Do you want to draw another card? Type 'y' or 'n': ").lower()
            # If the player chooses to continue drawing, add a new card to their hand.
            if drawing == 'y':
                user_cards.append(deal_card())
    # If the game has not ended yet, perform the final calculations.
    if not game_over:
        # Until the computer's score >= 16, they will continue to draw cards.
        while computer_score < 16:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        # Find out if either the user or computer won the game.
        game_state = compare(user_score, computer_score)
        print(f"Your hand is: {user_cards}, with a score of {user_score}.")
        print(f"The hand of the computer is: {computer_cards}, with a score of {computer_score}.")
        if game_state == 1:
            print("You win!")
        elif game_state == -1:
            print("You lose!")
        else:
            print("It's a draw!")
    # Ask the player if they want to continue playing.
    playing = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    # Clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')

# Thank the player for playing.    
print("Thank you for playing!")