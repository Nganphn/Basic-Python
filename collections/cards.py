# cards = []
# card = 1
# while card < 14:
#     cards.append(card)
#     card += 1

# cards[0] = "Ace"
# cards[10] = "Jack"
# cards[11] = "Queen"
# cards[12] = "King"

# clubs = cards.copy()
# diamonds = cards.copy()
# hearts = cards.copy()
# spades = cards.copy()

# for card in clubs:
#     print(card, "of Clubs")
# for card in diamonds:
#     print(card, "of Diamons")
# for card in hearts:
#     print(card, "of Hearts")
# for card in spades:
#     print(card, "of Spades")



# Define rank list
ranks = ["Ace"] + list(range(2,11)) + ["Jack", "Queen", "King"]

# Define suit list
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# Define deck
deck = []

# Build deck
for suit in suits:
    for rank in ranks:
        card = str(rank) + " of " + suit
        deck.append(card)

# Print cards individually
for card in deck:
    print(card)
print()


# # Define card list
# cards = ["Ace"] + list(range(2,11)) + ["Jack", "Queen", "King"]

# # Define suit list
# suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# # Define deck
# deck = [f"{card} of {suit}" for suit in suits for card in cards]

# for card in deck:
#     print(card)


import random

def shuffled():
    random.shuffle(deck)
    for card in deck:
        print(card)

shuffled()