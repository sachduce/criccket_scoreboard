from random import randint;
class Inning():
    BALLS_IN_OVER = 6;

    def __init__(self, number_of_overs, number_of_players, batsman, bowlers, target = None):
        super().__init__();
        self._batsman = batsman;
        self._bowlers = bowlers;
        self._extras = 0;
        self._wickets_fell = 0;
        self._max_balls = number_of_overs * Inning.BALLS_IN_OVER;
        self._max_wickets = number_of_players - 1;
        self._runs_scored = 0;
        self._balls_bowled = 0;
        self._is_over = False;
        self._striker = batsman[self._wickets_fell];
        self._non_striker = batsman[self._wickets_fell + 1];
        self._bowler = self._bowlers[randint(0, number_of_players - 1)];
        self._target = target;

    @property
    def extras(self):
        return self._extras;

    @property
    def is_over(self):
        return self._is_over;

    @property
    def runs_scored(self):
        return self._runs_scored + self._extras;

    @property
    def balls_bowled(self):
        return self._balls_bowled;

    @property
    def wickets_fell(self):
        return self._wickets_fell;

    def update_inning(self, ball):
        ball = ball.lower();
        if(self._is_over == False):
            if(ball == 'nb'):
                self._extras += 1;
            elif( ball == 'wd'):
                self._extras += 1;
            elif(ball == 'w'):
                self._wickets_fell += 1;
                self._balls_bowled += 1;
                self._striker.batting.update_batting_scores(ball);
                if(self._wickets_fell != self._max_wickets):
                    self._striker = self._batsman[self._wickets_fell+1];
            elif(ball.isnumeric()):
                score = int(ball);
                self._runs_scored += score;
                self._balls_bowled += 1;
                # update value for batting of player
                self._striker.batting.update_batting_scores(ball);
                # rotate player
                if(score % 2 == 1):
                    self._striker, self._non_striker = self._non_striker, self._striker;

            ## update bowler record
            self._bowler.bowling.update_bowling_scores(ball);
            if(self._wickets_fell == self._max_wickets or self._balls_bowled == self._max_balls or (self._target and self._target < self._runs_scored)):
                self._is_over = True;

            if (not self._is_over and self._balls_bowled % 6 == 0 and ball.isnumeric()):
                self._striker, self._non_striker = self._non_striker, self._striker;
                self._bowler = self._bowlers[randint(0, self._max_wickets)];

            if(self._is_over or (self._balls_bowled % 6 == 0 and ball.isnumeric())):
                self.print_innings();
        else:
            raise ValueError('Innings over for the team');


    def print_innings(self):
        print("Batting Scorecard for team:")
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Player Name", "Score", "Balls", "4s", "6s", "Strike Rate"));
        for p in self._batsman:
            p.print_player_batting(self._striker, self._non_striker);

        print("Bowling Scorecard for team:")
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}".format("Player Name", "Overs", "Runs", "Wickets", "Dots", "Economy"));
        for p in self._bowlers:
            p.print_player_bowling();

        print("Total : {}/{}".format(self.runs_scored, self._wickets_fell));
        print("Overs : {}.{}".format(self._balls_bowled // Inning.BALLS_IN_OVER,
                                     self._balls_bowled % Inning.BALLS_IN_OVER));
        print("Extras : {}".format(self._extras));









