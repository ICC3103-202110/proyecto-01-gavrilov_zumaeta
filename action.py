from player import Player
class Action:
    def _init_(self):
        self.__action_status=None
        self.__action_succes=True

    @property
    def action_status(self):
        return self.__action_status

    @action_status.setter
    def action_status(self,choice):
        self.__action_status=choice

    @property
    def action_succes(self):
        return self.__action_status

    @action_succes.setter
    def action_succes(self,choice):
        self.__action_succes=choice

    #public method
    def income(self,player):
            player.coins=1
            print("Plater {}  now has {} coins".format(player.name,player.coins))





