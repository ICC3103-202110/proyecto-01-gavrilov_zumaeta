from player import Player
from deck_of_cards import Deck_of_cards 
from console import Console
from action import Action
from counterattack import Counterattack
from random import shuffle

class Game:
    MAX_NUMBER_PLAYERS=4
    MIN_NUMBER_PLAYERS=3
    __players=[]
    __table_deck=None
    __current_player=None
    __list_of_actions=["Income","Foreign Help","Hit","Taxes","Murder","Extortion","Change"]
    __dic_of_influences={"Taxes":"Duke","Murder":"Assassin","Extortion":"Captain","Change":"Ambassador"}
    __number_of_players=0

    @classmethod
    def play(cls):
        cls.__set_players()
        cls.__set_deck()
        for player in cls.__players:
            cls.__table_deck.assign_cards_player(player,2,cls.__table_deck.deck)
        cls.__number_of_players=len(cls.__players)

        #We let everybody see their cards by turns
        print("\nOn this first round every player will get to SEE THEIR CARDS.")
        for player in cls.__players:
            player.status="Playing"
            print("PASS computer to {}".format(player))
            input("PLAYER {} PRESS ANY KEY to see your cards".format(player))
            player.see_cards()
            input("PRESS ANY KEY to continue")
            Console.clear()
            player.status=None
        
        #To not begin first round inmediately:
        print("Pass the computer to {}".format(cls.__players[0]))
        input("NOW THE GAME BEGINS: press any key")

        while len(cls.__players)>1:
            for player in cls.__players:
                if (player==cls.__current_player):
                    continue
                cls.__current_player=player
                cls.__player_play()
                cls.__remove_player()
        
        print("{} there are NO MORE PLAYERS left, YOU WON!!".format(cls.__players[0]))

    @classmethod
    def __player_play(cls):
        Console.clear()
        print("It's {}'s turn!".format(cls.__current_player))
        cls.__current_player.status="Playing"
        cls.__current_player.see_cards()
        cls.__see_coins_and_cards()
        flag=0
        while (flag==0):
            choice=Console.player_menu(cls.__current_player.name)
            flag= cls.__current_player.money_to_play(choice)

        action=Action()
        action.action_status=cls.__list_of_actions[choice-1]
        action.action_succes=True
        action.activity_log=[]
        input("PRESS ANY KEY AND PASS the computer to the other players")
        Console.clear()
        Console.show_last_action(cls.__current_player.name,action.action_status)
        action.activity_log.append("{} chose the action {}".format(cls.__current_player,action.action_status))

        if (choice!=1 and choice!=2 and choice!=3):
            cls.__challenge(cls.__current_player,action)
        cls.__remove_player()
        if action.action_succes==True:
            if (choice==2 or choice==5 or choice==6):
                result=cls.__counterattack(cls.__current_player,action.action_status)
                if result!=0:
                    action.activity_log.append("{} counterattacked {}".format(result[0],cls.__current_player))
                    new_counterattack=Counterattack(result[0],result[1])
                    new_counterattack.defy_counterattack(cls.__players,cls.__current_player,action,cls.__table_deck)

        if (action.action_succes==True):
            print("Now {} gets to complete their action".format(cls.__current_player))
            action.activity_log.append("{} got to complete the action {}".format(cls.__current_player,action.action_status))
            action.master_of_actions(choice,cls.__current_player,cls.__players,cls.__table_deck.deck)
        cls.__current_player.status=None
        input("Press any key to continue")
        Console.clear()
        Console.show_log(cls.__current_player,action.activity_log)
        input("END OF TURN, PRESS ANY KEY to continue")
        

    @classmethod
    def __see_coins_and_cards(cls):
        print("----------------------------------------")
        for i in cls.__players:
            Console.coins_and_cards_display(i.name,i.coins,i.cards[0],i.cards[1])
        print("----------------------------------------")


    @classmethod
    def __set_players(cls):
        number_players=input("Please enter number of players: \n")
        condition = 0
        while condition == 0:
            if number_players.isnumeric() == False:
                print("NOT VALID. Try with a number")
                number_players=input("Please enter number of players: \n")
            else:
                if int(number_players)<cls.MIN_NUMBER_PLAYERS:
                    number_players=3
                    print("Min. Nº of Players is 3! Go find some more people.")
                    condition = 1
                elif int(number_players)>cls.MAX_NUMBER_PLAYERS:
                    number_players=4
                    print("Max. Nº of Players is 4! Choose who stays.")
                    condition = 1
                for i in list(range(int(number_players))):
                    name=input("Player {} enter your name: ".format(i+1))
                    cls.__players.append(Player(name,i+1))
                    condition = 1

    @classmethod    
    def __set_deck(cls):
        cls.__table_deck=Deck_of_cards()

    @classmethod
    def __challenge(cls,player,action):
        print("Does anybody want to DEFY this action?")
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
        action.activity_log.append("{} challenged {}".format(challenger,player))
        print("{} you have been CHALLENGED by {}".format(player,challenger))
        win=False
        influence=cls.__dic_of_influences[action.action_status]
        
        #when winning a challenge your card gets inmediatly replaced wit one on the deck
        for card in player.cards:
            if (card.out_of_game==False):
                if card.influence==influence:
                    win=True
                    cls.__table_deck.deck.append(card)
                    player.cards.remove(card)
                    cls.__table_deck.assign_cards_player(player,1,cls.__table_deck.deck)
        
        if win==True:
            print("{} you have WON the challenge".format(player))
            input("press ANY KEY to see your new card")
            player.see_cards()
            input("press ANY KEY to continue AND PASS computer to {}".format(challenger))
            Console.clear()
            challenger.resign_card()
            action.activity_log.append("{} lost the challenge".format(challenger))
            action.action_succes=True
        else:
            print("{} you have lost the challenge".format(player))
            action.action_succes=False
            action.activity_log.append("{} lost the challenge".format(player))
            input("press ANY KEY to CONTINUE")
            Console.clear()
            player.resign_card()

        
    @classmethod
    def __counterattack(cls,player,action):
        counterattacks={"Foreign Help":["Duke"],"Murder":["Countess"], "Extortion":["Captain","Ambassador"]}
        print("You can COUNTERATTACK {}'s action if you have influence on: ".format(player))
        for element in counterattacks[action]:
            print(element)
        challengers=[]
        for other_player in cls.__players:
            if other_player.status!="Playing":
                add=input("{} PRESS 1 if you want to COUNTERATTACK, press any other key otherwise ".format(other_player))
                if add=="1":
                    challengers.append(other_player)
        if len(challengers)==0:
            print("Nobody counterattacked you")
            return 0
        shuffle(challengers)
        challenger=challengers[0]
        print("{} you have been COUNTERATTACKED by {}".format(player,challenger))
        if action=="Extortion":
            num_influence=int(input("{} SELECT 0 if you have influence on the CAPTAIN / SELECT 1 if you have influence over the AMBASSADOR: ".format(challenger)))
            influence=counterattacks[action][num_influence]
        else: 
            influence=counterattacks[action][0]
        challenger.status="Challenging"
        return [challenger,influence]
    
    @classmethod
    def __remove_player(cls):
        for player in cls.__players:
            counter=0
            for card in player.cards:
                if card.out_of_game==True:
                    counter+=1
            if counter==2:
                cls.__players.remove(player)


if __name__=="__main__":
   Game.play()
   
