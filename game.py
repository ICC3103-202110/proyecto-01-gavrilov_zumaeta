from player import Player
from deck_of_cards import Deck_of_cards 
from console import Console
from action import Action

class Game:
    MAX_NUMBER_PLAYERS=4
    MIN_NUMBER_PLAYERS=3
    __players=[]
    __table_deck=None
    __current_player=None
    __list_of_actions=["Income","Foreign Help","Hit","Taxes","Murder","Extortion","Change"]

    @classmethod
    def play(cls):
        cls.__set_players()
        cls.__set_deck()
        for player in cls.__players:
            cls.__table_deck.assign_cards_player(player,2,cls.__table_deck.deck)
        
        cls.__player_play()
        cls.__current_player=cls.__players[1]
        cls.__player_play()


    
    @classmethod
    def __player_play(cls):
        Console.clear()
        cls.__current_player.status="Playing"
        cls.__see_coins_and_cards()
        cls.__current_player.see_cards()
        choice=Console.player_menu(cls.__current_player.name)
        action=Action()
        action.action_status=cls.__list_of_actions[choice-1]
        input("Press any key and pass the computer to the other players")
        Console.clear()
        Console.show_last_action(cls.__current_player.name,action.action_status)
        if choice==1:
            action.income(cls.__current_player)
        if choice==2:
            action.foreign_help(cls.__current_player)
        if choice==3:
            action.hit(cls.__current_player,cls.__players)
        if choice==4:
            action.taxes(cls.__current_player)
        if choice==5:
            action.murder(cls.__current_player,cls.__players)
        if choice==6:
            action.extortion(cls.__current_player,cls.__players)
        if choice==7:
            action.change(cls.__current_player,cls.__table_deck.deck)

        cls.__current_player.status=None
        input("End of turn press any key to continue")
        

    @classmethod
    def __see_coins_and_cards(cls):
        for i in cls.__players:
            Console.coins_and_cards_display(i.name,i.coins,i.cards[0],i.cards[1])


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

    @classmethod    
    def __set_deck(cls):
        cls.__table_deck=Deck_of_cards()

if __name__=="__main__":
   Game.play()
   
