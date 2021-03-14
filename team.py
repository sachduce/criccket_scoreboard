from player import Player;


class Team:
    def __init__(self, number_of_players, name):
        self.number_of_players = number_of_players;
        self.name = name;
        self.players = [];


    def addPlayer(self, name):
        if(len(self.players) < self.number_of_players):
            self.players.append(Player(name));
        else:
            raise ValueError("Team Squad is full!!")




