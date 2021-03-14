class Player:
    def __init__(self, name):
        self.name = name;
        self._runs_scored = 0;
        self._balls_faced = 0;
        self._balls_bowled = 0;
        self._wickets_taken = 0;
        self._is_out = False;

    @property
    def runs_scored(self):
        return self._runs_scored

    @property
    def balls_faced(self):
        return self._balls_faced


    def update_scores(self, val):
        if(self._is_out == False):
            if(val == 'w'):
                self._is_out = True;
            else:
                self._runs_scored += val;
            self._balls_faced += 1;
        else:
            raise ValueError("Invalid update for player");




