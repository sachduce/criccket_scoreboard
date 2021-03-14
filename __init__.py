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

    result = m1.declare_winner();
    print(result);

