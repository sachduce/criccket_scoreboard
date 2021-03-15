class Batting:

    def __init__(self):
        self._runs_scored = 0;
        self._balls_faced = 0;
        self._fours = 0;
        self._sixes = 0;
        self._is_out = False;
        self._sccore_card = [0]* 12
#[0,0,0,0,4,0, 8, 8, 8, 8]
    @property
    def strike_rate(self):
        if (self._balls_faced == 0):
            return 0;
        return round(100 * self._runs_scored / self._balls_faced, 2);

    @property
    def runs_scored(self):
        return self._runs_scored;

    @property
    def balls_faced(self):
        return self._balls_faced;

    @property
    def sixes(self):
        return self._sixes;

    @property
    def fours(self):
        return self._fours;

    @property
    def is_out(self):
        return self._is_out;

    def update_batting_scores(self, val):
        if (self._is_out == False):
            if (val == 'w'):
                self._is_out = True;
            elif (val.isnumeric()):
                if (val == '4'):
                    self._fours += 1;
                if (val == '6'):
                    self._sixes += 1;
                self._runs_scored += int(val);
            self._balls_faced += 1;
        else:
            raise ValueError("Invalid update for player");
