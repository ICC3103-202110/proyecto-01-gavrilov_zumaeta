from player import Player
class Game:
    MAX_NUMBER_PLAYERS=4
    MIN_NUMBER_PLAYERS=3
    _players=[]
    _deck=[]
    _current_player=None

    @classmethod
    def play(cls):
        cls.set_players()
    @classmethod
    def set_players(cls):
        number_players=int(input("Please enter number of players: \n"))
        if number_players<cls.MIN_NUMBER_PLAYERS:
            number_players=3
        if number_players>cls.MAX_NUMBER_PLAYERS:
            number_players=4
        for i in list(range(number_players)):
            name=input("Player {} enter your name: ".format(i+1))
            cls._players.append(Player(name,i+1))
        


if __name__=="__main__":
   Game.play()
