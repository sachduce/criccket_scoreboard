from batting import Batting;
from bowling import Bowling;

class Player:
    def __init__(self, name):
        self.name = name;
        self.batting = Batting();
        self.bowling = Bowling();


    def print_player_batting(self, striker, non_striker):
        name = self.name + '*' if not self.batting._is_out and (self == striker or self == non_striker) else self.name;
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} ".
              format(name, self.batting._runs_scored, self.batting._balls_faced,
                     self.batting._fours, self.batting._sixes, self.batting.strike_rate));

    def print_player_bowling(self):
        print("{:<15}  {:<10} {:<10} {:<10} {:<10} {:<10} ".
              format(self.name, self.bowling.overs_bowled,  self.bowling._runs_conceded, self.bowling._wickets_taken,
                     self.bowling._dots, self.bowling.economy));
