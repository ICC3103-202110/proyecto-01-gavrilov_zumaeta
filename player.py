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
            for i in range(2):
                if self.cards[i].out_of_game==False:
                    self.cards[i].hidden=False
        print("[ This is {}'s turn. ] Your cards are: ".format(self.name))
        m=1
        for card in self.cards:
            if card.out_of_game==False:
                print("{}. {} you have the card {}".format(m,card))
            m+=1
        
        if self.status=="Playing":
            for i in range(2):
                if self.cards[i].out_of_game==False:
                    self.cards[i].hidden=True
    
    def resign_card(self):
        print("{} you ought to resign a card".format(self.__name))
        self.status="Playing"
        self.see_cards()
        card_resigned=int(input("press the number of the card you want to resign: "))
        self.cards[card_resigned-1].out_of_game=True
        self.status=None
        Console.clear()
    
    def money_to_play(self,choice):
        if (self.__coins==10 and choice !=3):
            print("Sorry you have 10 coins you ought to make a hit")
            return 0
        if (self.__coins<7 and choice ==3):
            print("Sorry you don´t have enough coins to make a hit")
            return 0
        if (self.__coins<3 and choice ==5):
            print("Sorry you don´t have enough coins to murder")
            return 0
        return 1
        


    def __str__(self):
        return self.__name


