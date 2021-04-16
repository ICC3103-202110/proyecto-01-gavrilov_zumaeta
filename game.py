from player import Player
from deck_of_cards import Deck_of_cards 
from console import Console
from action import Action
from random import shuffle

class Game:
    MAX_NUMBER_PLAYERS=4
    MIN_NUMBER_PLAYERS=3
    __players=[]
    __table_deck=None
    __current_player=None
    __list_of_actions=["Income","Foreign Help","Hit","Taxes","Murder","Extortion","Change"]
    __dic_of_influences={"Taxes":"Duke","Murder":"Assassin","Extortion":"Captain","Change":"Ambassador"}

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
        flag=0
        while (flag==0):
            choice=Console.player_menu(cls.__current_player.name)
            flag= cls.__current_player.money_to_play(choice)

        action=Action()
        action.action_status=cls.__list_of_actions[choice-1]
        action.action_succes=True
        input("Press any key and pass the computer to the other players")
        Console.clear()
        Console.show_last_action(cls.__current_player.name,action.action_status)
        if (choice!=1 and choice!=2 and choice!=3):
            cls.__challenge(cls.__current_player,action)
        if (action.action_succes==True):
            print("Now {} gets to complete their action".format(cls.__current_player))
            action.master_of_actions(choice,cls.__current_player,cls.__players,cls.__table_deck.deck)
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

    @classmethod
    def __challenge(cls,player,action):
        print("Does anybody want to defy this action?")
        challengers=[]
        for other_player in cls.__players:
            if other_player.status!="Playing":
                add=input("{} press 1 if you want to challenge, press any other key otherwise ".format(other_player))
                if add=="1":
                    challengers.append(other_player)
        if len(challengers)==0:
            print("Nobody challenged you")
            return 0
        shuffle(challengers)
        challenger=challengers[0]
        print("{} you have been challenged by {}".format(player,challenger))
        win=False
        influence=cls.__dic_of_influences[action.action_status]
        
        for card in player.cards:
            if (card.out_of_game==False):
                if card.influence==influence:
                    win=True
        
        if win==True:
            print("{} you have won the challenge".format(player))
            input("press any key to continue")
            Console.clear()
            challenger.resign_card()
            action.action_succes=True
        else:
            print("{} you have lost the challenge".format(player))
            action.action_succes=False
            input("press any key to continue")
            Console.clear()
            player.resign_card()

        




if __name__=="__main__":
   Game.play()
   
