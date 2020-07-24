import random

cards_values = { '2 Heart': 2, '3 Heart': 3, '4 Heart': 4, '5 Heart': 5, '6 Heart': 6, '7 Heart': 7, '8 Heart': 8,
                 '9 Heart': 9, '10 Heart': 10, 'Jack Heart': 10, 'Queen Heart': 10, 'King Heart': 10,
                 'Ace Heart': (1, 11), '2 Spade': 2, '3 Spade': 3, '4 Spade': 4, '5 Spade': 5, '6 Spade': 6,
                 '7 Spade': 7, '8 Spade': 8, '9 Spade': 9, '10 Spade': 10, 'Jack Spade': 10, 'Queen Spade': 10,
                 'King Spade': 10, 'Ace Spade': (1, 11), '2 Club': 2, '3 Club': 3, '4 Club': 4, '5 Club': 5,
                 '6 Club': 6, '7 Club': 7, '8 Club': 8, '9 Club': 9, '10 Club': 10, 'Jack Club': 10,
                 'Queen Club': 10, 'King Club': 10, 'Ace Club': (1, 11), '2 Diamond': 2, '3 Diamond': 3,
                 '4 Diamond': 4, '5 Diamond': 5, '6 Diamond': 6, '7 Diamond': 7, '8 Diamond': 8, '9 Diamond': 9,
                 '10 Diamond': 10, 'Jack Diamond': 10, 'Queen Diamond': 10, 'King Diamond': 10,
                 'Ace Diamond': (1, 11)
                 }
all_cards = ['2 Heart', '3 Heart', '4 Heart', '5 Heart', '6 Heart', '7 Heart', '8 Heart', '9 Heart',
             '10 Heart', 'Jack Heart', 'Queen Heart', 'King Heart', 'Ace Heart', '2 Spade', '3 Spade',
             '4 Spade', '5 Spade', '6 Spade', '7 Spade', '8 Spade', '9 Spade', '10 Spade', 'Jack Spade',
             'Queen Spade', 'King Spade', 'Ace Spade', '2 Club', '3 Club', '4 Club', '5 Club', '6 Club',
             '7 Club', '8 Club', '9 Club', '10 Club', 'Jack Club', 'Queen Club', 'King Club', 'Ace Club',
             '2 Diamond', '3 Diamond', '4 Diamond', '5 Diamond', '6 Diamond', '7 Diamond', '8 Diamond',
             '9 Diamond', '10 Diamond', 'Jack Diamond', 'Queen Diamond', 'King Diamond', 'Ace Diamond']


class Deck:
    def __init__(self, deck):
        self.deck = deck

    def hit(self):
        card = random.choice(self.deck)
        return card

    def remained(self, card):
        return self.deck.remove(card)


class Hands:
    def __init__(self, player):
        self.player = player

    def handvalue(self, card, value=0):
        value += cards_values[card]
        print(cards_values[card])
        return value


class Chips:

    def __init__(self, chip):
        self.chip = chip

    def remained_chip(self, bet):
        self.chip -= bet
        return self.chip
