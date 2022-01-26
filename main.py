import random, sys
card_values = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
card_colours = ["Diamonds", "Heart", "Spades", "Clubs"]


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self, shuffle=True):
        self.cards = []
        self.create_new_deck()
        if shuffle:
            self.shuffle()

    def create_new_deck(self):
        for suit in card_colours:
            for value in card_values:
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return "Deck is empty"


class Player():
    def __init__(self):
        self.all_cards  = []
    def add_card_to_hand(self):
        new_deck = Deck()
        self.all_cards.append(new_deck.deal_card())
        print(f"Your deck consists of {self.all_cards}")


class COM():
    def __init__(self):
        self.c_all_cards  = []
    def c_add_card_to_hand(self):
        c_new_deck = Deck()
        self.c_all_cards.append(c_new_deck.deal_card())
        print(f"COM'S deck consists of {self.c_all_cards}")


class BlackJack():
    def __init__(self):
        """Controls The Game"""
        self.score = 0
        self.c_score = 0
        self.player_b = Player()
        self.com_b = COM()
        while True:
            answer = input("Hit(H) or Stand(S): ")
            if answer == "H":
                self.player_b.add_card_to_hand()
                BlackJack.calc_score(self)
                if self.score > 21:
                    print("You Lost")
                    BlackJack.again_input(self)
                elif self.score == 21:
                    print("You Won")
                    BlackJack.again_input(self)
                else:
                    continue
            elif answer == "S":
                while True:
                    if self.c_score < 21:
                        if self.c_score > self.score:
                            print("COM Won")
                            BlackJack.again_input(self)
                        else:
                            self.com_b.c_add_card_to_hand()
                            BlackJack.c_calc_score(self)
                    elif self.c_score == 21:
                        print("COM Won")
                        BlackJack.again_input(self)    
                    elif self.c_score >21:
                        print("You Won")
                        BlackJack.again_input(self)
    
    def again_input(self):
        """When the game ends the player is asked whether they want to play again or not and it also resets both scores"""
        self.again_input = input("Do you want to play again?[Y/N]: ")
        if self.again_input == "Y":
            self.score = 0
            self.c_score = 0
            self.player_b.all_cards.clear()
            self.com_b.c_all_cards.clear()
            BlackJack()
        else:
            sys.exit()
    
    def calc_score(self):
        """Calculates Player's Score"""
        self.score = 0
        for i in self.player_b.all_cards:
            self.score += card_values[i.value]
        print(self.score)
    
    def c_calc_score(self):
        """Calculates COM's Score"""
        self.c_score = 0
        for j in self.com_b.c_all_cards:
            self.c_score += card_values[j.value]
        print(self.c_score)

BlackJack()
