first_player = input()
second_player = input()
first_player_points = 0
second_player_points = 0
command = ""

firs_player_card = input()
second_player_card = input()
while command != "End of game":
    firs_player_card = int(firs_player_card)
    second_player_card = int(second_player_card)
    if firs_player_card > second_player_card:
        first_player_points += firs_player_card - second_player_card
    elif second_player_card > firs_player_card:
        second_player_points += second_player_card - firs_player_card
    elif firs_player_card == second_player_card:
        print("Number wars")
        firs_player_card = int(input())
        second_player_card = int(input())
        if firs_player_card > second_player_card:
            first_player_points += firs_player_card - second_player_card
            print(f"{first_player} is winner with {first_player_points} points")
        elif second_player_card > firs_player_card:
            second_player_points += second_player_card - firs_player_card
            print(f"{second_player} is winner with {second_player_points} points")
            break

    firs_player_card = input()
    second_player_card = input()
print(f"{first_player} has {first_player_points} points")
print(f"{second_player} has {second_player_points} points")
