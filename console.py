import os
class Console:
    @staticmethod
    def player_menu(name):
        print("\nHere is the menu of actions\n")
        print("{:<20}{:>20}".format("General Actions:","Character Actions:"))
        print("{:<20}{:>16}".format(" 1.Income"," 4.Duch-Taxes "))
        print("{:<20}{:>20}".format(" 2.Foreign Help", " 5.Assassin-Murder"))
        print("{:<20}{:>22}".format(" 3.Hit", "  6.Captain-Extortion"))
        print("{:>42}".format(" 7.Ambassador-Change"))
        return int(input("\n{} choose the number of the Action you want to make: ".format(name)))

    @staticmethod
    def coins_and_cards_display(name,coins,card1,card2):
        print("{}'s coins: [{}] | {}'s cards: {} {}".format(name,coins,name,card1,card2))

    @staticmethod
    def clear():
        os.system('cls||clear')

    @staticmethod
    def show_last_action(name,action):
        print("Player {} has chosen the action {}".format(name,action))

