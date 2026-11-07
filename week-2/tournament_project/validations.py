
def is_empty(choice):
    if choice.strip():
        return False
    return True


def is_digits(choice):
    return choice.isdigit()

def is_in_range(choice, start, stop):
    return choice in range(start, stop)
        


def is_exist_team_id(team_id, teams):
    for team in teams:
        if team["id"] == team_id:
            return True
    return False


    
def is_exist_team_name(team_name, teams):
    for team in teams:
        if team["name"] == team_name:
            return True
    return False


def is_exist_and_diff(home_team_id, away_team_id):
    if home_team_id == away_team_id:
        return False

    if is_exist_team(home_team_id) and is_exist_team(away_team_id):
        return True
    return False

def is_first_meeting(home_team, away_team, maches):
    for mach in maches:
        if (mach["home_team_id"] == home_team and mach["away_team_id"] == away_team) or (mach["home_team_id"] == away_team and mach["away_team_id"] == home_team):
            return False
    return True



