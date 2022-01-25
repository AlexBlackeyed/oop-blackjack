import random,sys
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

class BlackJack():
    def __init__(self):
        """Controls The Game"""
        self.score = 0
        self.c_score = 0
        while True:
            answer = input("Hit(H) or Stand(S): ")
            if answer == "H":
                Player.add_card(self)
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
                            COM.add_card(self)
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
            BlackJack()
        else:
            sys.exit()
    
    def calc_score(self):
        self.score += card_values[player_random_card]
        print("Your Score: {}".format(self.score))
    
    def c_calc_score(self):
        self.c_score += card_values[com_random_card]
        print("Croupier's Score: {}".format(self.c_score))


class Player():  
    def __init__(self):
        pass
    
    def add_card(self):
        global player_random_card
        """Gets Random Card/Calculates its value and adds it to the total score"""
        self.random_colour= random.choice(card_colours)
        self.random_card = random.choice(list(card_values))
        print("Your New Card is {} of {}".format(self.random_card,self.random_colour) + " and its value is {}".format(card_values[self.random_card]))
        player_random_card = self.random_card


class COM():
    def __init__(self):
        pass
    
    def add_card(self):
        global com_random_card
        """Gets Random Card/Calculates its value and adds it to the total score"""
        self.c_random_colour = random.choice(card_colours)
        self.c_random_card = random.choice(list(card_values))
        print("Croupier's New Card is {} of {}".format(self.c_random_card,self.c_random_colour) + " and its value is {}".format(card_values[self.c_random_card]))
        com_random_card = self.c_random_card
        

BlackJack()
