"""Program to practice assert statements with specific message."""

import random

spam = random.randint(0, 30)
print('Spam = ' + str(spam))
assert spam >= 10, 'Spam needs to be greater than 10.'
