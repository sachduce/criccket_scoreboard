class Inning():
    BALLS_IN_OVER = 6;

    def __init__(self, number_of_overs, number_of_wickets, batsman, bowlers):
        super().__init__();
        self._batsman = batsman;
        self._bowlers = bowlers;
        self._extras = 0;
        self._wickets_fell = 0;
        self._max_balls = number_of_overs * Inning.BALLS_IN_OVER;
        self._max_wickets = number_of_wickets;
        self._runs_scored = 0;
        self._balls_bowled = 0;
        self._is_over = False;
        self._striker = batsman[self._wickets_fell];
        self._non_striker = batsman[self._wickets_fell + 1];

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
                self._striker.update_scores(ball);
                if(self._wickets_fell != self._max_wickets):
                    self._striker = self._batsman[self._wickets_fell+1];
            elif(ball.isnumeric()):
                score = int(ball);
                self._runs_scored += score;
                self._balls_bowled += 1;
                self._striker.update_scores(score);
                if(score % 2 == 1):
                    self._striker, self._non_striker = self._non_striker, self._striker;

            if(self._wickets_fell == self._max_wickets or self._balls_bowled == self._max_balls):
                self._is_over = True;

            if(not self._is_over and self._balls_bowled% 6 == 0):
                self._striker, self._non_striker = self._non_striker, self._striker;
        else:
            raise ValueError('Innings over for the team');


    def print_innings(self):
        print("Scorecard for team:")
        print("{:<15} {:<10} {:<10}".format("Player Name", "Score", "Balls"));
        for p in self._batsman:
            name = p.name + '*' if not p._is_out  and (p == self._striker or p == self._non_striker) else p.name;
            print("{:<15} {:<10} {:<10}".format(name, p.runs_scored, p.balls_faced));
        print("Total : {}/{}".format(self.runs_scored, self._wickets_fell));
        print("Overs : {}.{}".format(self._balls_bowled//Inning.BALLS_IN_OVER, self._balls_bowled%Inning.BALLS_IN_OVER ));









