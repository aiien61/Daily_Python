import random, logging
from enum import Enum, auto

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# logging.disable(logging.CRITICAL)

class Toss(Enum):
    TAILS = auto()
    HEADS = auto()
    

guess = ''
while guess not in [t.name for t in Toss]:
    print('Guess the coin toss. Enter heads or tails:')
    guess = input().upper()
    try:
        assert Toss[guess] == Toss.HEADS or Toss[guess] == Toss.TAILS, 'Invalid guess'
    except AssertionError:
        logging.error('Invalid guess. Try again.')


toss = random.randint(1, 2) # 1 is tails, 2 is heads
if Toss(toss).name == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().upper()
    try:
        assert Toss[guess] == Toss.HEADS or Toss[guess] == Toss.TAILS, 'Invalid guess'
    except AssertionError:
        logging.error('Invalid guess. Try again.')

    if Toss(toss).name == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
