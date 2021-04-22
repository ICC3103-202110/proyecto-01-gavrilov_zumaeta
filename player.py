from cards import Cards
from console import Console

class Player:
    def __init__(self,name,number):
        self.name=name
        self.__number=number
        self.__coins=2
        self.cards=[]
        self.__status=None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name=name
    
    @property
    def coins(self):
        return self.__coins
    
    @coins.setter
    def coins(self,value):
        self.__coins=self.__coins+value

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,stat):
        self.__status=stat

    def see_cards(self):
        if self.status=="Playing" or self.status=="Challenging":
            for i in range(len(self.cards)):
                if self.cards[i].out_of_game==False:
                    self.cards[i].hidden=False
        print("\n{} Your cards are: ".format(self.name))
        m=1
        for card in self.cards:
            if card.out_of_game==False:
                print("{}. {}".format(m,card))
            m+=1
        
        if self.status=="Playing" or self.status=="Challenging":
            for i in range(len(self.cards)):
                if self.cards[i].out_of_game==False:
                    self.cards[i].hidden=True

    def see_cards_option(self):
        print("=======================")
        print("PRESS 1 if you wish to SEE YOUR CARDS AGAIN. 0 if you don't.")
        print("You get this choice ONCE before choosing your action!")
        print("=======================")
        number = Console.cast(0,1)
        if number == 1:
            self.see_cards()
            input("To continue: press enter")
            Console.clear()
        else:
            return
    
    def resign_card(self):
        print("{} you ought to resign a card".format(self.__name))
        self.status="Playing"
        self.see_cards()
        print("Press the NUMBER of the card you want to resign: ")
        card_resigned = Console.cast(0,len(self.cards))
        self.cards[card_resigned-1].out_of_game=True
        self.status=None
        Console.clear()
    #checks if you have the money to complete a certain action
    def money_to_play(self,choice):
        if (self.__coins==10 and choice !=3):
            print("You have 10 COINS. You MUST CHOOSE HIT")
            return 0
        if (self.__coins<7 and choice ==3):
            Console.clear()
            print("\n==== NOT ENOUGH COINS for Hit. Try again. =====")
            return 0
        if (self.__coins<3 and choice ==5):
            Console.clear()
            print("\n==== NOT ENOUGH COINS for Murder. Try again. =====")
            return 0
        return 1

    def __str__(self):
        return self.__name


