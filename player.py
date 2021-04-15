from cards import Cards

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
        if self.status=="Playing":
            for i in range(2):
                self.cards[i].hidden=False

        print("{} your cards are: {} and {}".format(self.name,self.cards[0],self.cards[1]))
        
        if self.status=="Playing":
            for i in range(2):
                self.cards[i].hidden=True
    
    def resign_card(self):
        print("{} you ought to resign a card".format(self.__name))
        self.status="Playing"
        self.see_cards()
        card_resigned=int(input("press 1 to resign the first one, press 2 to resign the second one: "))
        self.cards[card_resigned-1].out_of_game=True
        print(self.cards[card_resigned-1].out_of_game)


    def __str__(self):
        return self.__name


