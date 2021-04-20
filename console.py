import os
class Console:
    @staticmethod
    def player_menu(name):
        print("\nHere is the menu of actions\n")
        print(": . _ . : . _ . : . _ . : . _ . : . _ . :")
        print("{:<20}{:>20}".format("General Actions:","Character Actions:"))
        print("{:<20}{:>16}".format(" 1.Income"," 4.Duch-Taxes "))
        print("{:<20}{:>20}".format(" 2.Foreign Help", " 5.Assassin-Murder"))
        print("{:<20}{:>22}".format(" 3.Hit", "  6.Captain-Extortion"))
        print("{:>42}".format(" 7.Ambassador-Change"))
        print(": . _ . : . _ . : . _ . : . _ . : . _ . :")
        
        value = input("\n{} choose the NUMBER of the Action you want to make:".format(name))
        while cast(value) == False or (int(value)< 1 or int(value)>7):
            print("Your answer is NOT VALID. Try again.")
            value = input("\n{} NOT VALID. Choose the NUMBER of the Action you want to make:".format(name))
        value = int(value)
        return value

    @staticmethod
    def coins_and_cards_display(name,coins,card1,card2):
        print("{}'s coins: {} | {}'s cards: {} {}".format(name,coins,name,card1,card2))

    @staticmethod
    def clear():
        os.system('cls||clear')

    @staticmethod
    def show_last_action(name,action):
        print("Player {} has chosen the action {}".format(name,action))

    @staticmethod
    def show_log(player,log_list):
        print("GAME LOG:")
        print("Here is what happend in {}'s turn".format(player))
        for element in log_list:
            print("• {}".format(element))
        print("Now {} has {} coins".format(player,player.coins))

    def cast(number):
        try:
            number = int(number)
            return number
        except ValueError:
            print ("NUMBER IS NOT VALID. Try again!")
            return False


