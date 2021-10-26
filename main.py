from random import choice

class Game_Handler:
    """
    Tools to assist in building card games\n
    Dealer Class:
    ---
    `Holds the deck of cards and deals with card disribution.`
    Player Class:
    ---
    `Object that stores the player variables.`
    """

    class Dealer:
        """
        Holds the deck of cards and deals with card disribution.

        Functions:
        ---
        `random_card()` - `Selects a random card within the deck.`
        `deal_cards(player, cards=2)` - `Deals an amount, cards, to a player.`
        """
        def __init__(self):
            self.Dealer = Game_Handler.Dealer
            # This is the deck of cards. 1 means the card is in the deck, 0 means the card is somewhere else.
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

        def random_card(self):
            """Selects a random card from the deck."""
            # Creates a list containing the suites with cards left.
            active_suites = []
            for suite in self.Deck:
                suite_total = 0
                for card in self.Deck[suite]:
                    suite_total += self.Deck[suite][card]
                if suite_total > 0:
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
        """
        Object that stores the player variables.
        Functions:
        ---
        `play_card(player, card: tuple)` - `Transfers a card to another player object.`\n
        `get_cards()` - `Returns a neater dictionary only containing the cards in the player hand.`
        """
        def __init__(self, player_name):
            self.name = player_name
            self.hand = {
                "Clubs": {},
                "Diamonds": {},
                "Spades": {},
                "Hearts": {}
            }
            
        def play_card(self, player, card: tuple):
            """
            Transfers a card to another player object.\n
            Recieves the card in the tuple format: (Suite, Card). `Ex:("Hearts", "Ace")`.
            """
            suite, card = card[0], card[1]
            if self.hand[suite][card] == 1:
                self.hand[suite].update({card: 0})
                player.hand[suite].update({card: 1})
            else:
                print(f"Card does not exist within {self.name}'s hand.")
            
        def get_cards(self):
            """Returns a neater dictionary only containing the cards in the player hand."""
            cards = dict()
            # Updates the active suites in the cards dictionary.
            for suite in self.hand:
                suite_total = 0
                for card in self.hand[suite]:
                    suite_total += self.hand[suite][card]
                if suite_total > 0:
                    cards.update({suite: {}})
            
            # Updates the active cards to the proper suite in the cards dictionary.
            for suite in self.hand:
                for card in self.hand[suite]:
                    if self.hand[suite][card] == 1:
                        cards[suite].update({card: 1})
            
            # Return the updated cards dictionary.
            return cards
