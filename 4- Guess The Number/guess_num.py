import random;
import os

def clear_screen():
  """
  Function to clear the command line interface.
  """
  # Check the operating system
  if os.name == 'nt':  # For Windows
      os.system('cls')
  else:  # For Linux and macOS
      os.system('clear')

def game_start():
  while True:
    difficulty = input('Select Difficulty (Easy, Medium or Hard): ').lower()
    if difficulty in ['easy', 'medium', 'hard']:
      break
    else:
      print('Invalid Difficulty')

  if difficulty == 'easy':
    maxRange = 10
    return maxRange
  elif difficulty == 'medium':
    maxRange = 15
    return maxRange
  elif difficulty == 'hard':
    maxRange = 25
    return maxRange


def player_guess():
  while True:
    player = input('Take a Guess: ')
    try:
      player = int(player)
      if player < 1 or player > maxRange:
        print('Please type a number within the range')
      else:
        return player
    except ValueError:
      print('Please type a number')

def start_game():
  player_name = input('The player\'s name: ')
  
  pc = random.randint(1, maxRange)

  print(f'The number is between 1 and {maxRange}')

  player = player_guess()

  attempts = 1

  while pc != player:
    if pc > player:
      print('Hint: Higher')
      player = player_guess()
      attempts += 1
    else:
      print('Hint: lower')
      player = player_guess()
      attempts += 1
  else:
    print(f'You Won! it took you {attempts} Attempts')


maxRange = game_start()

start_game()

while True:
  restart = input('Would you like to play again? (y/n) ').lower()
  if restart != 'y' and restart != 'yes' and restart != 'n' and restart != 'no':
    print('Invalid Response')
  elif restart == 'y' or restart == 'yes':
    clear_screen()
    maxRange = game_start()
    start_game()
  else:
    clear_screen()
    break