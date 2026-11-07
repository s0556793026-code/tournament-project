
from  data_teams import teams, matches

from validations import is_digits, is_exist_and_diff, is_exist_team_id, is_first_meeting, is_empty, is_digits, is_in_range, is_exist_team_name

from o_i import input_user


def get_and_validate_choice():
    valid_choice = False
    while not valid_choice:
        user_choice = input("Choose an option: ")
        if not is_digits(user_choice):
            print("Choice must be an integer. Try again\n")
            continue
        user_choice = int(user_choice)
        if not is_in_range(user_choice, 0,11):
            print("Choice must be 0-10 Try again\n")
            continue
        return user_choice


def get_and_validate_team_id():
    valid_id = False
    while not valid_id:
        team_id = input("Enter team ID: ")
        if not is_digits(team_id):
            print("ID must be a positive integer\n")
            continue
        team_id = int(team_id)
        if is_exist_team_id(team_id, teams):
            print("ID is alredy exist. try again\n")
            continue
        return team_id



def get_and_validate_team_name():
    while True:
        team_name = input("Enter team name: ")
        if is_empty(team_name):
            print("Name cannot be empty")
            continue
        if is_exist_team_name(team_name, teams):
            continue
            print("Name is alredy exist. try again\n")
        return team_name


def add_team_details(team_id, team_name):
    teams.append({
    "id": team_id, "name": team_name, "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
    })
    print("Team added succssfully")


def show_teams():
    if not teams:
            print("There are not teams in the list yet")
            return
    for team in teams:
        print(f"team id: {team["id"]}\nteam name: {team["name"]}\nplayed: {team["played"]}\npoints: {team["points"]}\n")
        print()


def input_and_validate_game(): # לסדר את הפונקציה
    while True:
        home_id = input("Enter home team id: ")
        away_id = input("Enter away team id: ")
        if is_exist_and_diff(home_id, away_id) and is_first_meeting(home_id, away_id, matches):
            break
        print("teams must be different")

    while True:
        home_goals = input("Enter teh home team goals")
        if is_digits(home_goals):
            home_goals = int(home_goals)
            break
        print("goal must be an positive integer")

    while True:
        away_goals = input("Enter teh away team goals")
        if is_digits(away_goals):
            away_goals = int(away_goals)
            break
        print("goal must be an positive integer")
    
    return home_id, away_id, home_goals, away_goals

def add_game_result(home_id,away_id,home_goals,away_goals ):
    matches.append({"home_team_id": home_id, "away_team_id": away_id, "home_goals": home_goals, "away_goals": away_goals})
    


