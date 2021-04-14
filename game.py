from player import Player
from deck_of_cards import Deck_of_cards 
from console import Console

class Game:
    MAX_NUMBER_PLAYERS=4
    MIN_NUMBER_PLAYERS=3
    __players=[]
    __table_deck=None
    __current_player=None

    @classmethod
    def play(cls):
        cls.__set_players()
        cls.__set_deck(cls)
        for player in cls.__players:
            cls.__table_deck.assign_cards_player(player,2,cls.__table_deck.deck)
        cls.__player_play()
    
    @classmethod
    def __player_play(cls):
        Console.clear()
        action=Console.player_menu(cls.__current_player.name)


        


    @classmethod
    def __set_players(cls):
        number_players=int(input("Please enter number of players: \n"))
        if number_players<cls.MIN_NUMBER_PLAYERS:
            number_players=3
        if number_players>cls.MAX_NUMBER_PLAYERS:
            number_players=4
        for i in list(range(number_players)):
            name=input("Player {} enter your name: ".format(i+1))
            cls.__players.append(Player(name,i+1))
        cls.__current_player=cls.__players[0]
        
    def __set_deck(cls):
        cls.__table_deck=Deck_of_cards()

if __name__=="__main__":
   Game.play()
   
