import random

#from random import shuffle
#from IPython.display import clear_output


class Deck:
    def __init__(self, card):
        self.card = card

    def deck_create(self):
        self.card = []
        suits = (" Clubs", "Diamonds", "Hearts", "Spades.")
        card = []

        for suit in suits:
            for value in range(1, 14):             
                self.card.append(str(value + suit)               
    print(self.card)



    def shuffle(self):
        print(random.shuffle(self.card))
        
    def drawing_cart(self)
        
        


deck = Deck([])
deck.deck_create()
deck.shuffle

# # create a deck and randomly shuffle
# deck = list(range(1,53))
# random.shuffle(deck)
# print(deck)