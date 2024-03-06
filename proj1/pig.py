import random as rand

player_amount = int(input("How many players (2-4): "))
rolling = False

scoreboard = {}

player_number = 1

while True:
    if player_amount < 2:
        print("You need 2-4 players to play this game.")
        player_amount = int(input("How many players (2-4): "))
    else:
        break

# Populate dictionary
for player in range(1, player_amount+1):
    scoreboard[f'Player {player}'] = 0

rolling = True

while rolling:
    confirm = input(f"Would you like to roll (Player {player_number}): ")
    
    roll_number = rand.randint(1,6)
    
    if roll_number == 1:
        print(f"Aw shucks! You rolled a 1! Player {player_number}'s turn is done!")
        if player_amount > player_number:
            player_number += 1
            print()
            print(f"It's your turn Player {player_number}!")
            print()
        else:
            break
    else:
        scoreboard[f'Player {player_number}'] += roll_number
        print(f"Player {player_number} score is: {scoreboard[f'Player {player_number}']}")
  
print("**** FINAL SCORES ****")   
max_score = max(scoreboard.values())   

for player, score in scoreboard.items():
    print(f"{player}: {score}")

tie = [key for key, value in scoreboard if value == max_score]

print(tie)

print(f"Winner: {max(scoreboard.keys())}")
print("**********************")


        
    
    
    
    
        
    
        
        