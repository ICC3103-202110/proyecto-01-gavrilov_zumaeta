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
        if stat in ["Playing","Challenge","Fight_back","pass"]:
            self.__status=stat




