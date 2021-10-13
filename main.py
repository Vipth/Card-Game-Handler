from random import choice

class Game_Handler:
    """
    Tool to assist in building card games. Has the classes:\n
    `Dealer`\n
    `player`
    """

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
            return self.suite, self.card

        def deal_cards(self, player, cards=2):
            """Deals cards."""
            for _ in range(cards):
                suite, card = self.random_card()
                player.hand[suite].update({card: 1})

    class Player:
        """Object that stores the player variables."""
        def __init__(self, name):
            self.name = name
            self.hand = {
                "Clubs": {},
                "Diamonds": {},
                "Spades": {},
                "Hearts": {}
            }

        def play_card(self, player, card: tuple): # Tuple in format of (Suite, Card), Ex: ("Hearts", "Ace")
            """Transfers a card to another player object."""
            suite, card = card[0], card[1]
            if self.hand[suite][card] == 0:
                self.hand[suite].update({card: 0})
                player.hand[suite].update({card: 1})
            else:
                print(f"Card does not exist within {self.name}'s hand.")

        def get_cards(self):
            # I want to make this function return a smaller list or dictionary with the players cards, so it's more readable.
            pass
