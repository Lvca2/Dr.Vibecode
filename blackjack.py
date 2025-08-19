import random

# Define card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]  # Ace can be either 1 or 11
}

# Define the deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = card_values[rank] if rank != 'A' else card_values[rank]  # Aces are special

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

# Hand class to manage a player's or dealer's cards
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def calculate_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            if card.rank == 'A':
                ace_count += 1
                value += 11
            else:
                value += card.value
        # Adjust for aces if value exceeds 21
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def display(self, show_all=True):
        if show_all:
            return ', '.join([str(card) for card in self.cards])
        else:
            return f"{self.cards[0]} and Hidden Card"

# Function to handle the player's turn (Hit or Stand)
def player_turn(player_hand, deck):
    while True:
        print(f"Your hand: {player_hand.display()} - Total: {player_hand.calculate_value()}")
        choice = input("Do you want to Hit or Stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.add_card(deck.deal())
            if player_hand.calculate_value() > 21:
                print(f"Your hand: {player_hand.display()} - Total: {player_hand.calculate_value()}")
                print("Busted! You went over 21.")
                return False
        elif choice == 's':
            return True
        else:
            print("Invalid choice. Please enter 'h' to Hit or 's' to Stand.")

# Function to handle the dealer's turn
def dealer_turn(dealer_hand, deck):
    while dealer_hand.calculate_value() < 17:
        print(f"Dealer's hand: {dealer_hand.display(show_all=False)} - Total: {dealer_hand.calculate_value()}")
        print("Dealer hits.")
        dealer_hand.add_card(deck.deal())
    print(f"Dealer's final hand: {dealer_hand.display()} - Total: {dealer_hand.calculate_value()}")
    return dealer_hand.calculate_value() <= 21

# Function to determine the winner
def determine_winner(player_hand, dealer_hand):
    player_value = player_hand.calculate_value()
    dealer_value = dealer_hand.calculate_value()

    print(f"Your final hand: {player_hand.display()} - Total: {player_value}")
    print(f"Dealer's final hand: {dealer_hand.display()} - Total: {dealer_value}")

    if player_value > 21:
        return "You busted! Dealer wins."
    elif dealer_value > 21:
        return "Dealer busted! You win."
    elif player_value > dealer_value:
        return "You win!"
    elif player_value < dealer_value:
        return "Dealer wins!"
    else:
        return "It's a tie!"

# Main function to play the game
def play_blackjack():
    print("Welcome to Blackjack!\n")

    # Initialize deck, hands, and deal cards
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    print(f"Dealer's hand: {dealer_hand.display(show_all=False)} - Total: {dealer_hand.calculate_value()}")
    
    # Player's turn
    if not player_turn(player_hand, deck):
        print("You busted! Dealer wins.")
        return

    # Dealer's turn
    if not dealer_turn(dealer_hand, deck):
        print("Dealer busted! You win.")
        return

    # Determine winner
    result = determine_winner(player_hand, dealer_hand)
    print(result)

# Run the game
if __name__ == "__main__":
    play_blackjack()
