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

    class Card_Interpreter:
        Card: str
        def return_card_value(self, Card, high_ace=False):
            if "Ace" in Card:
                if high_ace == True:
                    return 14
                else:
                    return 1
            elif "Two" in Card:
                return 2
            elif "Three" in Card:
                return 3
            elif "Four" in Card:
                return 4
            elif "Five" in Card:
                return 5
            elif "Six" in Card:
                return 6
            elif "Seven" in Card:
                return 7
            elif "Eight" in Card:
                return 8
            elif "Nine" in Card:
                return 9
            elif "Ten" in Card:
                return 10
            elif "Jack" in Card:
                return 11
            elif "Queen" in Card:
                return 12
            elif "King" in Card:
                return 13

    class create_player:
        """Object that stores the player variables."""
        hand: list
        def __init__(self, player_name):
            self.name = player_name