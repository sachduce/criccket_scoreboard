from batting import Batting;
from bowling import Bowling;

class Player:
    def __init__(self, name):
        self.name = name;
        self.batting = Batting();
        self.bowling = Bowling();


    def print_player_batting(self, striker, non_striker):
        name = self.name + '*' if not self.batting.is_out and (self == striker or self == non_striker) else self.name;
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} ".
              format(name, self.batting.runs_scored, self.batting.balls_faced,
                     self.batting.fours, self.batting.sixes, self.batting.strike_rate));

    def print_player_bowling(self):
        print("{:<15}  {:<10} {:<10} {:<10} {:<10} {:<10} ".
              format(self.name, self.bowling.overs_bowled,  self.bowling.runs_conceded, self.bowling.wickets_taken,
                     self.bowling.dots, self.bowling.economy));
