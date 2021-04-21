from console import Console
# # def cast(start,stop):
# #     number= input("Enter your number:")
# #     flag = True
# #     while flag:
# #         if not number.isnumeric():
# #             print ("NUMBER IS NOT VALID. Try again!")
# #             number= input("Enter your number:")
# #         else:
# #             number = int(number)
# #             if number not in range(start,stop):
# #                 print("NUMBER IS NOT VALID. Try again!")
# #                 number= input("Enter your number:")
# #             else:
# #                 flag = False
# #                 return number

# # def actionchooser():        
# #     print("Choose the NUMBER of the Action you want to make:")
# #     return cast(1,8)

# # a = actionchooser()
# # b = actionchooser()
# #
# #print(a+b)


# print(": . _ . : . _ . : . _ . : . _ . : . _ . :")
# print("{:<20}{:>20}".format("General Actions:","Character Actions:"))
# print("{:<20}{:>13}".format(" 1.Income"," 4.Duke:Tax"))
# print("{:<20}{:>21}".format(" 2.Foreign Help", " 5.Assassin: Murder"))
# print("{:<20}{:>23}".format(" 3.Hit", "  6.Captain: Extortion"))
# print("{:>42}".format(" 7.Ambassador-Change"))
# print(": . _ . : . _ . : . _ . : . _ . : . _ . :")

# print("What they do:")
# print("1) Take 1 coin.")
# print("2) Take 2 coins.")
# print("3) Pay 7 coins and choose a Player to loose influence.")
# print("4) Take 3 Coins. Also blocks foreign aid.")
# print("5) Pay 3 coins and choose a Player to loose influence.")
# print("6) Take 2 coins from another player.")
# print("7) Exchange cards with court deck.")

cards = [1,2,3,4]
def see_cards(wuhu):
    m=0
    for card in cards:
        print("{}. something".format(m))
        m+=1
    
def resign_card():
    print("Press the NUMBER of the card you want to resign: ")
    card_resigned = Console.cast(0,m)
    print(card_resigned)

see_cards(cards)
print(len(cards))
resign_card()