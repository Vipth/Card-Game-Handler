from random import choice

class Game_Handler:

    class Dealer:
        """Handles card distribution and organization."""
        def __init__(self):
            self.Dealer = Game_Handler.Dealer
            # This is the deck of cards. 0 means the card is in the deck, 0 means the card is somewhere else.
            self.Deck = {
            "Clubs": {
                "Ace": 1,
                "Two": 1,
                "Three": 1,
                "Four": 1,
                "Five": 1,
                "Six": 1,
                "Seven": 1,
                "Eight": 1,
                "Nine": 1,
                "Ten": 1,
                "Jack": 1,
                "Queen": 1,
                "King": 1
            },
            "Diamonds": {
                "Ace": 1,
                "Two": 1,
                "Three": 1,
                "Four": 1,
                "Five": 1,
                "Six": 1,
                "Seven": 1,
                "Eight": 1,
                "Nine": 1,
                "Ten": 1,
                "Jack": 1,
                "Queen": 1,
                "King": 1
            },
            "Spades": {
                "Ace": 1,
                "Two": 1,
                "Three": 1,
                "Four": 1,
                "Five": 1,
                "Six": 1,
                "Seven": 1,
                "Eight": 1,
                "Nine": 1,
                "Ten": 1,
                "Jack": 1,
                "Queen": 1,
                "King": 1
            },
            "Hearts": {
                "Ace": 1,
                "Two": 1,
                "Three": 1,
                "Four": 1,
                "Five": 1,
                "Six": 1,
                "Seven": 1,
                "Eight": 1,
                "Nine": 1,
                "Ten": 1,
                "Jack": 1,
                "Queen": 1,
                "King": 1
            }
        }

        # Currently throws an error when the deck is out of cards. I'm not sure how/when shuffling works in poker, so i'm going to wait to program that.
        def random_card(self):
            """Selects a random card from the deck."""

            # Creates a list containing the suites with cards left.
            active_suites = []
            for suite in self.Deck:
                self.suite_total = 0
                for card in self.Deck[suite]:
                    self.suite_total += self.Deck[suite][card]
                if self.suite_total > 0:
                    active_suites.append(suite)
            
            # Picks a suite from the list created above.
            self.suite = choice(active_suites)

            # Creates a list of active cards from the suite chosen from above.
            active_cards_in_list = []
            for card in self.Deck[self.suite]:
                if self.Deck[self.suite][card] == 1:
                    active_cards_in_list.append(card)

            # Picks a card from the list created above.
            self.card = choice(active_cards_in_list)

            # Removes card from Deck
            self.Deck[self.suite][self.card] = 0

            # Returns the card that has been chosen.
            return f'{self.card} of {self.suite}'

        def deal_cards(self, player, cards=2):
            """Deals cards."""
            player.hand = [self.Dealer.random_card(self) for _ in range(cards)]

    class create_player:
        """Object that stores the player variables."""
        hand: list
        def __init__(self, player_name):
            self.name = player_name
        
# Example for using this lib:

# Initialize the dealer.
Dealer = Game_Handler().Dealer()

# Create the player(s).
players = {
    "p1": Game_Handler().create_player("Vipth"),
    "p2": Game_Handler().create_player("Player 2")
}

# For this example we have two players, so we will deal them both half of the deck.
# You cannot exceed the amount of cards in a standard deck (52).
for player in players:
    Dealer.deal_cards(players[player], 6)

# Print both players hands.
for player in players:
    print(f"{players[player].name}: {players[player].hand}")