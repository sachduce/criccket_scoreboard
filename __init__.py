from sys import  stdin;
from match import Match;
if __name__ =='__main__':
    print("************** Start Match **************");
    print("Enter Number of Overs");
    number_of_overs = int(input());
    print("***** Number of overs in match : {} overs ********".format(number_of_overs));
    print("Enter Number of players in each team");
    number_of_players = int(input());
    print("***** Number of players in each side : {} players ********".format(number_of_players));
    m1 = Match(number_of_overs, number_of_players);
    print("***** Enter batting order for first team *****");
    for i in range(m1.number_of_players):
        m1.team1.addPlayer(input());
    print("***** Enter batting order for second team *****");
    for i in range(m1.number_of_players):
        m1.team2.addPlayer(input());

    m1.start_innings();
    print("***** Start first innings *****");
    while(not m1.inning1.is_over):
        # print("{} {} {}".format(m1.inning1.is_over, m1.inning1.runs_scored, m1.inning1.balls_bowled));
        m1.inning1.update_inning(input());

    m1.inning1.print_innings();

    print("***** End first innings *****");

    print("***** Start second innings *****");
    while (not m1.inning2.is_over):
        m1.inning2.update_inning(input());

    m1.inning2.print_innings();
    print("***** End Second innings *****");

    result = m1.declare_winner();
    print(result);

