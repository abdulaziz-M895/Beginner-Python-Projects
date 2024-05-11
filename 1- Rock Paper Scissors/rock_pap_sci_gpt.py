from random import choice

options = ['rock', 'paper', 'scissors']
pc = choice(options)

while True:
  user = input('Pick (rock | paper | scissors): ').lower()
  if user not in options:
    print('Invalid input. Please choose from rock, paper, or scissors.')
  else:
    break

print(f'Computer: {pc} | You: {user}')


if pc == user:
    print("It's a Draw!")
elif (pc == 'rock' and user == 'scissors') or \
    (pc == 'paper' and user == 'rock') or \
    (pc == 'scissors' and user == 'paper'):
    print('Computer Wins!')
else:
    print('You Win!')