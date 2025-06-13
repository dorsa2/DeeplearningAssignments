import random

# Possible choices
choices = ['rock', 'paper', 'scissors']

# Function to decide winner between two choices
def decide_winner(choice1, choice2):
    if choice1 == choice2:
        return 'Tie'
    elif (choice1 == 'rock' and choice2 == 'scissors') or \
         (choice1 == 'scissors' and choice2 == 'paper') or \
         (choice1 == 'paper' and choice2 == 'rock'):
        return 'Player 1 wins'
    else:
        return 'Player 2 wins'

# Simulate 10 rounds
rounds = 10
results = []

for i in range(1, rounds + 1):
    player1_choice = random.choice(choices)
    player2_choice = random.choice(choices)
    result = decide_winner(player1_choice, player2_choice)
    results.append((player1_choice, player2_choice, result))
    print(f"Round {i}: Player 1 chose {player1_choice}, Player 2 chose {player2_choice} -> {result}")
