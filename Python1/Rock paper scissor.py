import random


Game_Dic = {'stone': 1, 'paper': 2, 'scissor': 3}
player_points = 0
computer_points = 0


while player_points < 5 and computer_points < 5:
    computer_choice = random.randint(1, 3)
    player_choice = input()
    if Game_Dic[player_choice] == 1:
        if computer_choice == 2:
            computer_points += 1
        elif computer_choice == 3:
            player_points += 1
    elif Game_Dic[player_choice] == 2:
        if computer_choice == 1:
            player_points += 1
        elif computer_choice == 3:
            computer_points += 1
    else:
        if computer_choice == 1:
            computer_points += 1
        elif computer_choice == 2:
            player_points += 1
    print('Player score = ', player_points)
    print('Computer score = ', computer_points)


if player_points == 5:
    print("YOU WIN!!!!")
else:
    print("YOU LOSE:(:(BETTER LUCK NEXT TIME:):)")



