import csv

def load_csv_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to display 2022 Matches Regular Season
def view_2022_regular_season(matches):
    print("\nRegular Season 2022 Matches:")
    print("{:<30} {:<30} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
        "Home", "Away", "Date", "Year", "Time", "Home Score", "Away Score"))

    for match in matches:
        print("{:<30} {:<30} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
            match['home'], match['away'], match['date'], match['year'],
            match['time (utc)'], match['home_score'], match['away_score']))

# Function to display 2022 Matches Formations
def view_2022_formations(matches):
    print("\nFormations for 2022 Matches:")
    print("{:<30} {:<30} {:<15} {:<10} {:<10} {:<15} {:<15}".format(
        "Home", "Away", "Date", "Year", "Time", "Home Formation", "Away Formation"))

    for match in matches:
        print("{:<30} {:<30} {:<15} {:<10} {:<10} {:<15} {:<15}".format(
            match['home'], match['away'], match['date'], match['year'],
            match['time (utc)'], match['home_formation'], match['away_formation']))

# Function to display player statistics
def display_player_stats(players, season, column):
    if season == 'reg':
        print(f"\n{season.capitalize()} Season {column.capitalize()}:")
    elif season == 'pos':
        print(f"\nPost Season {column.capitalize()}:")

    for player in players:
        if int(player[column]) > 0:  # Check if the value is greater than zero
            print(f"{player['Player']} - Club: {player['Club']}, {column}: {player[column]}")

def display_goalkeeper_stats(goalkeepers, season, column):
    if season == 'reg':
        print(f"\nRegular Season {column.capitalize()}:")
    elif season == 'pos':
        print(f"\nPost Season {column.capitalize()}:")

    for goalkeeper in goalkeepers:
        if int(goalkeeper[column]) > 0:  # Check if the value is greater than zero
            print(f"{goalkeeper['Player']} - Club: {goalkeeper['Club']}, {column}: {goalkeeper[column]}")


def view_team_standings(standings, year):
    print(f"Viewing Team Standings for {year}:")
    print("Pos, Team, GP, W, L, SW, GF, GA, GD, Pts")
    for team in standings:
        if team['Year'] == str(year):
            print(f"{team['Pos']}, {team['Team']}, {team['GP']}, {team['W']}, {team['L']}, {team['SW']}, {team['GF']}, {team['GA']}, {team['GD']}, {team['Pts']}")


# Main function
def main():
    matches = load_csv_data('matches.csv')
    standings = load_csv_data('all_tables.csv')
    players = load_csv_data('all_players.csv')
    goalkeepers = load_csv_data('all_goalkeepers.csv')

    while True:
        print("\nChoose an option:")
        print("1. View Match Data")
        print("2. View Team Standings")
        print("3. Analyze Player Performance")
        print("4. Analyze Goalkeeper Performance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nChoose an option:")
            print("1. 2022 Matches Regular Season")
            print("2. 2022 Matches Formations")
            print("3. Exit")

            match_choice = input("Enter your choice: ")

            if match_choice == '1':
                view_2022_regular_season(matches)
            elif match_choice == '2':
                view_2022_formations(matches)
            elif match_choice == '3':
                pass  # Go back to main menu
            else:
                print("Invalid choice. Please choose a valid option.")

        elif choice == '2':
            print("\nChoose an option:")
            print("1. 2020 Standings MLS")
            print("2. 2021 Standings MLS")
            print("3. Exit")

            standings_choice = input("Enter your choice: ")

            if standings_choice == '1':
                view_team_standings(standings, year=2020)
            elif standings_choice == '2':
                view_team_standings(standings, year=2021)
            elif standings_choice == '3':
                pass  # Go back to main menu
            else:
                print("Invalid choice. Please choose a valid option.")

        elif choice == '3':
            print("\nAnalyze Player Performance:")
            print("Choose an option:")
            print("1. Regular Season 2020")
            print("2. Post Season 2022")
            print("3. Exit")

            player_performance_choice = input("Enter your choice: ")

            if player_performance_choice == '1':
                print("\nChoose an option:")
                print("1. Goalscorers")
                print("2. Assists")
                print("3. Yellow Cards")
                print("4. Red Cards")
                print("5. Exit")

                player_stat_choice = input("Enter your choice: ")

                if player_stat_choice == '1':
                    display_player_stats(players, season='reg', column='G')
                elif player_stat_choice == '2':
                    display_player_stats(players, season='reg', column='A')
                elif player_stat_choice == '3':
                    display_player_stats(players, season='reg', column='YC')
                elif player_stat_choice == '4':
                    display_player_stats(players, season='reg', column='RC')
                elif player_stat_choice == '5':
                    pass  # Go back to analyze player performance menu
                else:
                    print("Invalid choice. Please choose a valid option.")

            elif player_performance_choice == '2':
                print("\nChoose an option:")
                print("1. Goalscorers")
                print("2. Assists")
                print("3. Yellow Cards")
                print("4. Red Cards")
                print("5. Exit")

                player_stat_choice = input("Enter your choice: ")

                if player_stat_choice == '1':
                    display_player_stats(players, season='pos', column='G')
                elif player_stat_choice == '2':
                    display_player_stats(players, season='pos', column='A')
                elif player_stat_choice == '3':
                    display_player_stats(players, season='pos', column='YC')
                elif player_stat_choice == '4':
                    display_player_stats(players, season='pos', column='RC')
                elif player_stat_choice == '5':
                    pass  # Go back to analyze player performance menu
                else:
                    print("Invalid choice. Please choose a valid option.")

            elif player_performance_choice == '3':
                pass  # Go back to main menu

            else:
                print("Invalid choice. Please choose a valid option.")

        elif choice == '4':
            print("\nAnalyze Goalkeeper Performance:")
            print("Choose an option:")
            print("1. Regular Season 2020")
            print("2. Post Season 2020")
            print("3. Exit")

            goalkeeper_performance_choice = input("Enter your choice: ")

            if goalkeeper_performance_choice == '1':
                print("\nChoose an option:")
                print("1. Player Clean Sheets")
                print("2. Player Saves")
                print("3. Exit")

                goalkeeper_stat_choice = input("Enter your choice: ")

                if goalkeeper_stat_choice == '1':
                    display_goalkeeper_stats(goalkeepers, season='reg', column='SHTS')
                elif goalkeeper_stat_choice == '2':
                    display_goalkeeper_stats(goalkeepers, season='reg', column='SV')
                elif goalkeeper_stat_choice == '3':
                    pass  # Go back to analyze goalkeeper performance menu
                else:
                    print("Invalid choice. Please choose a valid option.")

            elif goalkeeper_performance_choice == '2':
                print("\nChoose an option:")
                print("1. Player Clean Sheets")
                print("2. Player Saves")
                print("3. Exit")

                goalkeeper_stat_choice = input("Enter your choice: ")

                if goalkeeper_stat_choice == '1':
                    display_goalkeeper_stats(goalkeepers, season='pos', column='SHTS')
                elif goalkeeper_stat_choice == '2':
                    display_goalkeeper_stats(goalkeepers, season='pos', column='SV')
                elif goalkeeper_stat_choice == '3':
                    pass  # Go back to analyze goalkeeper performance menu
                else:
                    print("Invalid choice. Please choose a valid option.")

            elif goalkeeper_performance_choice == '3':
                pass  # Go back to main menu

            else:
                print("Invalid choice. Please choose a valid option.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

