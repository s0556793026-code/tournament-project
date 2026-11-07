from logic import input_and_validate_game, add_game_result,  add_team_details, get_and_validate_choice, show_teams, get_and_validate_team_id, get_and_validate_team_name
from menu import choose_main_menu

# לזכור לשמור את ההוספות לרשימה בקובץ שנשמר ולא בליסט רגיל שנמחק מיד


def main():
    while True:
        choose_main_menu()
        choice = get_and_validate_choice()

        if choice == 1:
            team_id = get_and_validate_team_id()
            team_name = get_and_validate_team_name()
            add_team_details(team_id, team_name)
            continue
  
        elif choice == 2:
            show_teams()
            continue

        elif choice == 3:
            home_id, away_id, home_goal, away_goal = input_and_validate_game()
            add_game_result(home_id, away_id, home_goal, away_goal)

        elif choice == 4:
            pass

        elif choice == 5:
            pass

        elif choice == 6:
            pass

        elif choice == 7:
            pass

        elif choice == 8:
            pass

        elif choice == 9:
            pass

        elif choice == 10:
            pass

        else:
            break



if __name__=="__main__":
    main()

    