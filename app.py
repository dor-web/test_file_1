import constants
import random

#runs the main program
def main_menu():

    team_dirs = clean_data(team = constants.TEAMS, player = constants.PLAYERS)
    choices = 1

    #Create main menu for user to see teams in league or leave
    print("\nWelcome to the Basketball League!")
    print("--------------------------------------\n")
    print("----MENU----\n\n")
    while choices != 2:
        try:
            choices = int(input("""Here are your choices: \n 
                    1) Display Team Stats
                    2) Quit \n"""))       
            print("-------------------------------------------------\n")
            if choices == 1:
                choose_team()
                display_team(team_dirs)
            elif choices == 2:
                print('Good Bye!')
            elif choices > 2:
                print('Please enter 1 or 2,\n')
        except ValueError:
            print('Please enter 1 or 2.\n')
    return


#shows the teams in the league
def choose_team():

    for index, bb_team in enumerate(constants.TEAMS, 1):
        print(f'{index}.', bb_team)
        index += 1
    return

#display the team the users chooses
def display_team(team_dirs):
    
    while True:
        try:
            view_team = int(input("Pick a team you would like to see. "))
            print("-------------------------------------------------\n")
            if view_team < 1 or view_team > 3:
                print('Please enter the values that are provided.\n')
                choose_team()
                continue
            if view_team == 1:
                print("Team: Panthers")
                print("-------------------------------------------------\n")
                display_team_members(team_dirs, view_team,team = constants.TEAMS)
                break
            elif view_team == 2:
                print("Team: Bandits")
                print("-------------------------------------------------\n")
                display_team_members(team_dirs, view_team,team = constants.TEAMS)
                break
            elif view_team == 3:
                print("Team: Warriors")
                print("-------------------------------------------------\n")
                display_team_members(team_dirs, view_team,team = constants.TEAMS)
                break
        except ValueError:
            print('Please enter the values that are provided.\n')
            choose_team()
    return


#check to make sure each team has equal number of players
def clean_data(**kwargs):
    teams = kwargs['team']
    players = kwargs['player']
    
    team_dirs = {}
    player_dics = {}
    check_roster = {}

    number_players = len(players) #18 players
    number_teams = len(teams) #3 teams
    player_per_team = int(number_players/number_teams) #6 players to a team checks the number of players on the team
    max_roster = 0

    for player in players:
        for key,value in player.items():
            if key == 'name':
                player_dics[value] = player # {'Karl Saygan': {'experience': 'YES', 'guardians': 'Heather Bledsoe', 'height': '42 inches', 'name': 'Karl Saygan'}}
                break

    players_list = random.sample(list(player_dics.keys()),len(list(player_dics.keys())))

    for roster_list in teams: #get access to team name [Panther, Bandit, Warriors]
        num_experience = 0
        num_inexperience = 0
        player_count = 0
        player_stats = []  #player_stats[{player: stats}]

        for player in players_list:
            stats = {}
            stats.update(player_dics[player])
            if player_count == player_per_team: break
            if player in check_roster: continue
            if stats['experience'] == 'YES' and num_experience < 3:
                player_stats.append(stats)
                num_experience += 1
                player_count += 1
                max_roster += 1
                check_roster.update({player:stats})
            elif stats['experience'] == 'NO' and num_inexperience < 3:
                player_stats.append(stats)
                num_inexperience += 1
                player_count += 1
                max_roster += 1
                check_roster.update({player:stats})
            team_dirs[roster_list] = player_stats
    return team_dirs


def display_team_members(team_dirs, view_team, team):

    players = []
    names = []
    guardians = []
    heights = []
    experience = []

    sum_player_heights = 0
    num_experience = 0
    num_inexperience = 0

    team_picked = team[view_team-1]

    [players.append(value) for value in team_dirs[team_picked]]
    [names.append(value['name']) for value in players]
    [guardians.append(value['guardians']) for value in players]
    guardians = ', '.join(guardians).replace(' and ', ', ')
    [heights.append(int(value['height'].replace('inches', ''))) for value in players]
    [experience.append(value['experience']) for value in players]

    for player_heights in heights:
        sum_player_heights += player_heights
    avg_team_heights =  sum_player_heights/len(heights)

    for player_experience in experience:
        if player_experience == 'YES':
            num_experience += 1
        elif player_experience == 'NO':
            num_inexperience += 1
    
    print(f'Number of Player: {len(names)}','\n', 'Number of experience players: ', num_experience,'\n', 'Number of inexperience players: ', num_inexperience,'\n\n' 'Players on the team: \n', ', '.join(names), '\n')
    print(f'Guardians of Player: ', '\n', guardians, '\n')
    print('Average height of the team: \n {:.2f}'.format(avg_team_heights))
    print("-------------------------------------------------\n")
    return


if __name__ == "__main__":
    #start program
    main_menu()
