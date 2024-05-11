import random
import os

def clear_screen():
    """
    Function to clear the command line interface.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def game_start():
    """
    Function to select game difficulty.
    """
    while True:
        difficulty = input('Select Difficulty (Easy, Medium, or Hard): ').lower()
        if difficulty in ['easy', 'medium', 'hard']:
            break
        else:
            print('Invalid Difficulty')

    if difficulty == 'easy':
        return 10
    elif difficulty == 'medium':
        return 25
    elif difficulty == 'hard':
        return 40

def player_guess(max_range):
    """
    Function for player's guess.
    """
    while True:
        try:
            player = int(input(f'Take a Guess (1 - {max_range}): '))
            if 1 <= player <= max_range:
                return player
            else:
                print('Please type a number within the range')
        except ValueError:
            print('Please type a number')

def start_game(player_scores):
    """
    Function to start the game.
    """
    player_name = input('The player\'s name: ').capitalize()

    max_range = game_start()
    pc = random.randint(1, max_range)
    print(f'The number is between 1 and {max_range}')

    attempts = 0
    while True:
        attempts += 1
        player = player_guess(max_range)

        if pc > player:
            print('Hint: Higher')
        elif pc < player:
            print('Hint: Lower')
        else:
            print(f'You Won! it took you {attempts} Attempts')
            if player_name in player_scores:
                if attempts < min(player_scores[player_name], default=float('inf')):
                    player_scores[player_name] = attempts
            else:
                player_scores[player_name] = attempts
            break

if __name__ == "__main__":
    player_scores = {}

    clear_screen()
    while True:
        start_game(player_scores)
        restart = input('Would you like to play again? (y/n) ').lower()
        if restart in ['n', 'no']:
            clear_screen()
            print("Player scores:")
            for player, score in player_scores.items():
                print(f"{player}: {score} attempts")
            highest_score_player = min(player_scores, key=player_scores.get)
            highest_score = player_scores[highest_score_player]
            print(f"Highest Score: {highest_score_player} - {highest_score} attempts")
            break
        clear_screen()