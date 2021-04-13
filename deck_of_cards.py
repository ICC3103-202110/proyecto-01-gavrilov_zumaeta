from random import shuffle
from cards import Cards

class Deck_of_cards:
    
    def __init__(self):
        self.__deck=self.__create_deck()
    
    @property
    def deck(self):
        return self.__deck
    #private methods
    
    def __create_deck(self):
        roles=["Duke","Assassin","Captain","Ambassador","Countess"]
        deck=[]
        for element in roles:
            for i in range(3):
                deck.append(Cards(element))
        shuffle(deck)
        return deck

    def assign_cards_player (self,player,number,deck):
        for j in range(number):
            player.cards.append(deck[-1])
            deck.pop()

    def __str__(self):
        return self.__deck


