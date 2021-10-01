from random import choice

class CardHandler:
    """Handles card distribution and organization."""
    def __init__(self):
        # This is the deck of cards. 1 means the card is in the deck, 0 means the card is in someones hand.
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

        # Creates a list containing the suites with cards left
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

    def generate_board_cards(self, amount=5):
        """Generates the board cards and returns them as a list."""

        return [CardHandler.random_card(self) for x in range(amount)]

Deck = CardHandler()
print(Deck.generate_board_cards())