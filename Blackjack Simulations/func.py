from math import factorial
import numpy as np

# combinations formula
def C(n, r):
    return factorial(n) / (factorial(r)*(factorial(n-r)))

# permuations formula
def P(n, r):
    return factorial(n) / factorial(n-r)


# initialize n deck(s) of 52 cards
def get_decks(shuffle=True):
    deck = np.array((list(range(2,11))*4) + (["J", "Q", "K", "A"]*4))
    
    if shuffle:
        for _ in range(100):
            np.random.shuffle(deck)

    return deck