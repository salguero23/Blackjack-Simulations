from func import get_decks
import numpy as np

x = get_decks()
print(x)
print(f'selected card: {x[np.random.randint(52)]}')