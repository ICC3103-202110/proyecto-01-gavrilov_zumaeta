from random import shuffle
from console import Console


class Counterattack:
    def __init__(self,adversary,character):
        self.__adversary=adversary
        self.__character=character

    @property
    def adversary(self):
        return self.__adversary
    
    @adversary.setter
    def adversary(self,name):
        self.__adversary=name
    

    @property
    def character(self):
        return self.__character
    
    @character.setter
    def character(self,name):
        self.__character=name

    @property
    def succes(self):
        return self.__succes
    
    def master_of_counterattack(self,player,adversary,action):
        print("{} you have been COUNTERATTACKED by {}".format(player,adversary))
        if action=="Murder":
            self.countess(player)
        if (action=="Extortion" or action=="Foreign Help"):
            self.block_stealing_help(player)
    
    def defy_counterattack(self,list_of_players,player,action,table_deck):
        print("\nDoes anybody want to DEFY this COUNTERATTACK?")
        challengers=[]
        for other_player in list_of_players:
            if other_player.status!="Challenging":
                add=input("{} PRESS 1 if you want to CHALLENGE, press any other key otherwise ".format(other_player))
                if add=="1":
                    challengers.append(other_player)
        if len(challengers)==0:
            action.action_succes=False
            print("Nobody challenged you")
            self.master_of_counterattack(player,self.__adversary,action.action_status)
            return 0
        shuffle(challengers)
        challenger=challengers[0]
        action.activity_log.append("{} challenged {}'s counterattack".format(challenger,self.__adversary))
        print("{} you have been CHALLENGED by {}".format(self.__adversary,challenger))
        win=False
        for card in self.adversary.cards:
            if (card.out_of_game==False and card.influence==self.__character):
                win=True
                print("{} you have WON the CHALLENGE and get to complete the counterattack".format(self.__adversary))
                action.activity_log.append("{} won challenge and got to complete counterattack".format(self.__adversary))
                table_deck.deck.append(card)
                self.__adversary.cards.remove(card)
                table_deck.assign_cards_player(self.__adversary,1,table_deck.deck)
                input("{} press ANY KEY to see your new card".format(self.__adversary))
                self.__adversary.see_cards()
                input("PASS computer to {} AND PRESS ANY KEY to continue".format(challenger))
                Console.clear()
                challenger.resign_card()
                Console.clear()
                action.action_succes=False
                self.master_of_counterattack(player,self.__adversary,action.action_status)
        
        if win==False:
            print("{} you have LOST the CHALLENGE".format(self.__adversary))
            action.activity_log.append("{} won the challenge and got to stop the counterattack".format(challenger))
            input("PASS computer to {} AND PRESS ANY KEY to continue".format(self.__adversary))
            Console.clear()
            self.__adversary.resign_card()
            Console.clear()

        self.__adversary.status=None

    
    @succes.setter
    def succes(self,value):
        self.__succes=value
    
    def countess(self,player):
        print("Therefore {} you have LOST 3 COINS".format(player))
        player.coins=-3
    
    def block_stealing_help(self,player):
        print("Therefore {} you WON'T GET ANY COINS".format(player))
    

