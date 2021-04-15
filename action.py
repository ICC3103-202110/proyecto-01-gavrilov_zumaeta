from player import Player
from console import Console
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
        counter=0
        for person in (list_of_players):
            if person.status != "Playing":
                choose_person.append(person)
                print("You can take a hit on {} by pressing {}".format(person,counter))
                counter+=1

        hit_person=int(input("Enter the number of the person you want to hit: "))
        print("pass the computer to {}".format(choose_person[hit_person].name))
        input("press any key to continue")
        Console.clear()
        choose_person[hit_person].resign_card()
    
    def foreign_help(self,player):
        player.coins=2
        print("Player {} now has {} coins".format(player.name,player.coins))
    
    def taxes(self,player):
        player.coins=3
        print("Player {} now has {} coins".format(player.name,player.coins))
    
    def murder(self,player,list_of_players):
        player.coins=-3
        choose_person=[]
        counter=0
        for person in (list_of_players):
            if person.status != "Playing":
                choose_person.append(person)
                print("You can murder an influence of {} by pressing {}".format(person,counter))
                counter+=1

        murder_person=int(input("Enter the number of the person's influence you want to murder: "))
        print("pass the computer to {}".format(choose_person[murder_person].name))
        input("press any key to continue")
        Console.clear()
        choose_person[murder_person].resign_card()
        print("Player {} now has {} coins".format(player.name,player.coins))
    
    def extortion(self,player,list_of_players):
        choose_person=[]
        counter=0
        for person in (list_of_players):
            if person.status != "Playing":
                choose_person.append(person)
                print("You can extort {} by pressing {}".format(person,counter))
                counter+=1

        extort_person=int(input("Enter the number of the person you want to extort: "))
        if choose_person[extort_person].coins>=2:
            choose_person[extort_person].coins=-2
            player.coins=2
        elif (choose_person[extort_person].coins==1):
            choose_person[extort_person].coins=-1
            player.coins=1
        else:
            print("Sorry, this person had no coins")
        print("Player {} now has {} coins".format(player.name,player.coins))
        print("Player {} now has {} coins".format(choose_person[extort_person].name,choose_person[extort_person].coins))

    
    def change(self,player,deck):
        number_of_cards=0
        for card_player in player.cards:
            if card_player.out_of_game==False:
                number_of_cards+=1
        temporary_cards=[]

        for counter in range(2):
            deck[counter-1].hidden=False
            temporary_cards.append(deck[counter-1])

        for card in player.cards:
            if card.out_of_game==False:
                card.hidden=False
                temporary_cards.append(card)
        print("You get to keep {} cards out of these: ".format(number_of_cards))
        for num,element in enumerate(temporary_cards):
            print("{} to keep {}".format(num,element))
        
        new_cards_player=[]
        picked=[]
        for i in range(number_of_cards):
            pick=int(input("Enter number of card you wish to keep: "))
            if (pick==0 or pick==1):
                temporary_cards[pick].hidden=True
                new_cards_player.append(temporary_cards[pick])
                deck.pop(pick-1)
            else:
                temporary_cards[pick].hidden=True
                new_cards_player.append(temporary_cards[pick])
            picked.append(pick)
        
        for card in player.cards:
            if card.out_of_game==False:
                if card not in new_cards_player:
                    card.hidden=True
                    deck.append(card)
                    player.cards.remove(card)
        
        for card in new_cards_player:
            if card not in player.cards:
                player.cards.append(card)
        
        for card_deck in deck:
            card_deck.hidden=True

        player.see_cards()



        



    


        







