class Cards:
    def __init__(self,role):
        self.__influence=role
        self.__hidden=True
        self.__out_of_game=False

    def __str__(self):
        return self.__influence