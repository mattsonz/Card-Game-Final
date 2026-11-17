'''
The idea behind the code is to replicate Riding the Bus, the classic card game.
For anyone unfamiliar, the game starts with a player guessing the color of the card.
Followed by the value of the card being higher or lower than the initial card.
The third step is to guess whether the next card is between the two previous cards in value.
Finally, the player guesses the suit of the card. 
If the player guesses correctly, they move on to the next step.
if they guess incorrectly at any point, they are sent back to the beginning.
The game concludes when the player guesses all four steps correctly.

Challenges: 
Importing random elements for each step
Building the for loop
Other potential elements
Comparing values of strings to integers
'''
import random

# Opener Lists
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Face cards into integers so they can be compared
reframe = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'Jack': 11, 'Queen': 12,
    'King': 13, 'Ace': 14
}

deck = [(value, suit) for value in values for suit in suits]

# Deck shuffle, outside loop means that the game can end, but there is no card repeats
random.shuffle(deck)

while True:
    
    card = deck.pop()
    color_card = "red" if card[1] in ["Hearts", "Diamonds"] else "black"
    color = input("Guess the color of the card (Red or Black): ")
    if color.lower() == color_card:
        print(f"Your card is {card[0]} of {card[1]}.")
        step2 = input("Correct! Guess higher or lower now: ")
        card2 = deck.pop()
        if step2.lower() == "higher":
            beats = reframe[card2[0]] > reframe[card[0]]
        elif step2.lower() == "lower":
            beats = reframe[card2[0]] < reframe[card[0]]
        if beats == True:
            print(f"Your card is the {card2[0]} of {card2[1]}.")
            inside_outside = input("Is the next card between the previous two, or outside? (inside/outside) ")
            card3 = deck.pop()
            low = min(reframe[card[0]], reframe[card2[0]])
            high = max(reframe[card[0]], reframe[card2[0]])
            if inside_outside.lower() == "inside":
                beats2 = (low < reframe[card3[0]] and high > reframe[card3[0]])
            elif inside_outside.lower() == "outside":
                beats2 = (low > reframe[card3[0]] or high < reframe[card3[0]])
            if beats2 == True:
                card4 = deck.pop()
                print(f"Your card is the {card3[0]} of {card3[1]}!")
                final_suit = input("Correct! Finally, guess the suit of your last card: ")
                if final_suit.lower() == card4[1].lower():
                    print(f"Your final card is the {card4[0]} of {card4[1]}.")
                    play_again = input("You have rode the bus! Play again? (y/n)")
                    if play_again.lower() == 'y':
                        continue
                    else:
                        print("Nice Job!")
                        break
                else:
                    print(f"Incorrect! The card was the {card4[0]} of {card4[1]}")
                    play_again = input("Do you want to play again? (y/n): ")
                    if play_again.lower() == 'y':
                        continue
                    else:
                        print("Thanks for playing")
                        break
            else: 
                print(f"Incorrect! The card was the {card3[0]} of {card3[1]}.")
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() == "y":
                    continue
                else:
                    print("Thanks for playing!")
                    break
        else:
            print(f"Incorrect! The card was the {card2[0]} of {card2[1]}.")
            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() == "y":
                continue
            else:
                print("Thanks for playing!")
                break
    else:
        print(f"Incorrect! The card was the {card[0]} of {card[1]}.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            print("Thanks for playing!")
            break





