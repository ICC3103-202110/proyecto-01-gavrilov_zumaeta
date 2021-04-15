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
        print("Player {} now has {} coins".format(player.name,player.coins))
    
    def hit (self,player,list_of_players):
        player.coins=-7
        choose_person=[]
        for count,person in enumerate(list_of_players):
            if person.status != "Playing":
                choose_person.append(person)
                print("You can take a hit on {} by pressing {}".format(person,count))
        hit_person=int(input("Enter the number of the person you want to hit: "))
        choose_person[hit_person-1].resign_card()

        







