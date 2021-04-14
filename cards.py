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

    def __str__(self):
        if self.__hidden==False:
            return self.__influence
        if self.__hidden==True:
            return "[X]"

