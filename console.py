import os
class Console:

    @staticmethod
    def player_menu(name):
        print("\nHere is the menu of actions\n")
        print(": . _ . : . _ . : . _ . : . _ . : . _ . :")
        print("{:<20}{:>20}".format("General Actions:","Character Actions:"))
        print("{:<20}{:>14}".format(" 1.Income"," 4.Duke: Tax"))
        print("{:<20}{:>21}".format(" 2.Foreign Help", " 5.Assassin: Murder"))
        print("{:<20}{:>23}".format(" 3.Hit (Coup)", "  6.Captain: Extortion"))
        print("{:>45}".format(" 7.Ambassador: Exchange"))
        print(": . _ . : . _ . : . _ . : . _ . : . _ . :")
        
        value = input("\n{} choose the NUMBER of the Action you want to make:".format(name))
        while value.isnumeric() == False or (int(value)< 1 or int(value)>7):
            print("Your answer is NOT VALID. Try again.")
            value = input("Number of Action:")
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
        print("• Player {} has chosen the action {} •".format(name,action))

    @staticmethod
    def show_log(player,log_list):
        print("GAME LOG:")
        print("Here is what happend in {}'s turn".format(player))
        for element in log_list:
            print("• {}".format(element))
        print("• Now {} has {} coins".format(player,player.coins))

    @staticmethod
    def cast(start,stop):
        number= input("Enter your number:")
        flag = True
        while flag:
            if not number.isnumeric():
                print ("NUMBER IS NOT VALID. Try again!")
                number= input("Enter your number:")
            else:
                number = int(number)
                if number not in range(start,stop+1):
                    print("NUMBER IS NOT VALID. Try again!")
                    number= input("Enter your number:")
                else:
                    flag = False
                    return number


