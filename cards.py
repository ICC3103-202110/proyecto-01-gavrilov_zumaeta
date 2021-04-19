class Cards:
    def __init__(self,role):
        self.__influence=role
        self.__hidden=True
        self.__out_of_game=False

    @property 
    def hidden(self):
        return self.__hidden
    
    @hidden.setter
    def hidden(self,value):
        self.__hidden=value
    @property 
    def influence(self):
        return self.__influence

    @property 
    def out_of_game(self):
        return self.__out_of_game
    
    @out_of_game.setter
    def out_of_game(self,value):
        self.__out_of_game=value
#the card will only show itself on the table if the player lost its influence
    def __str__(self):
        if (self.__out_of_game==True):
            return self.__influence
        if (self.__hidden==False):
            return self.__influence
        if self.__hidden==True:
            return "[X]"
