from random import choice

class Game_Handler:
    """
    Tool to assist in building card games\n
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
            # We'll store the buy in money within the Dealer class.
            self.prize_pool = 0
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


    class Card_Hierarchy:
        # 1. Royal Flush
        # 2. Straight Flush
        # 3. Four of a kind
        # 4. Full house
        # 5. Flush
        # 6. Straight 
        # 7. Three of a kind
        # 8. Two pair
        # 9. Pair
        # 10. High Card

        def change_to_number(self, hand, high_ace=False):
            suite = list(hand.keys())
            cards_list = []
            if len(suite) == 1:
                for i in range(len(suite) + 1):
                    cards = suite[0]
                    cards_list.append(list(hand[cards])[i])
            else:
                for i in range(len(suite)):
                    cards = suite[i]
                    cards_list.append(list(hand[cards])[0])
            
            card_values = []
            for i in range(len(cards_list)):
                if "Ace" in cards_list[i]:
                    if high_ace == True:
                        card_values.append(14)
                    else:
                        card_values.append(1)
                elif "Two" in cards_list[i]:
                    card_values.append(2)
                elif "Three" in cards_list[i]:
                    card_values.append(3)
                elif "Four" in cards_list[i]:
                    card_values.append(4)
                elif "Five" in cards_list[i]:
                    card_values.append(5)
                elif "Six" in cards_list[i]:
                    card_values.append(6)
                elif "Seven" in cards_list[i]:
                    card_values.append(7)
                elif "Eight" in cards_list[i]:
                    card_values.append(8)
                elif "Nine" in cards_list[i]:
                    card_values.append(9)
                elif "Ten" in cards_list[i]:
                    card_values.append(10)
                elif "Jack" in cards_list[i]:
                    card_values.append(11)
                elif "Queen" in cards_list[i]:
                    card_values.append(12)
                elif "King" in cards_list[i]:
                    card_values.append(13)
                
            print(cards_list)
            print(card_values)
