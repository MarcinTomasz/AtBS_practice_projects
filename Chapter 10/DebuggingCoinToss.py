"""Coin toss guessing game."""

import random

guess = ''
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads

#lines 12-15 are my solution to the problem.
if toss == 1:
    toss = 'heads'
else:
    toss = 'tails'
    
if toss == guess:
  print('You got it!')
 else:
  print('Nope! Guess again!')
  guess = input()
  if toss == guess:
    print('You got it!')
   else:
    print('Nope. You are really bad at this game.')
    
