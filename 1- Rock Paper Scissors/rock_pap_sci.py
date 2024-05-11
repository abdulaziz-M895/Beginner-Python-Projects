from random import choice

pc = choice(['rock', 'paper', 'scissors'])

user = input('Pick ( rock | paper | scissors ): ')

print(f'Computer: {pc} |', f'You: {user}')

if pc == 'rock' and user == 'scissors':
  print('Computer Wins!')
elif pc == 'paper' and user == 'rock':
  print('Computer Wins!')
elif pc == 'scissors' and user == 'paper':
  print('Computer Wins!')
elif pc == user:
  print('Draw!')
else:
  print('You Win!')
