from team import Team;
from inning import Inning;

class Match:
    def __init__(self, number_of_overs, number_of_players):
        if (number_of_players < 2):
            raise ValueError('Number of players should be more than 1');
        self.number_of_overs = number_of_overs;
        self.number_of_players = number_of_players;
        self.team1 = Team(self.number_of_players, name='team1');
        self.team2 = Team(self.number_of_players, name='team2');

    def start_innings(self):
        self.inning1 = Inning(self.number_of_overs, self.number_of_players-1, self.team1.players, self.team2.players);
        self.inning2 = Inning(self.number_of_overs, self.number_of_players-1, self.team2.players, self.team1.players);

    def declare_winner(self):
        if(self.inning1.is_over and self.inning2.is_over):
            margin = abs(self.inning1.runs_scored - self.inning2.runs_scored);
            if(self.inning1.runs_scored  > self.inning2.runs_scored):
                return "{} won the match by {}".format(self.team1.name, margin);
            elif(self.inning1.runs_scored > self.inning2.runs_scored):
                return "{} won the match by {}".format(self.team2.name, margin);
            else:
                return "No Result!! Match is tied"
        else:
            return "Match in progress!!";





