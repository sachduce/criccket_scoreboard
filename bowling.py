class Bowling:

    BALLS_IN_OVER = 6;
    def __init__(self):
        self._runs_conceded = 0;
        self._balls_bowled = 0;
        self._wickets_taken = 0;
        self._dots = 0;


    @property
    def economy(self):
        if (self._balls_bowled == 0):
            return 'NA';
        return round((self._runs_conceded * Bowling.BALLS_IN_OVER)/(self._balls_bowled), 2);

    @property
    def overs_bowled(self):
        return "{}.{}".format(self._balls_bowled//Bowling.BALLS_IN_OVER, self._balls_bowled%Bowling.BALLS_IN_OVER )

    def update_bowling_scores(self, val):
        if (val == 'w'):
            self._wickets_taken += 1;
            self._balls_bowled += 1;
        elif(val == 'wd' or val == 'nb'):
            self._runs_conceded += 1;
        elif (val.isnumeric()):
            if(val == '0'):
                self._dots += 1;
            self._balls_bowled += 1;
            self._runs_conceded += int(val);


