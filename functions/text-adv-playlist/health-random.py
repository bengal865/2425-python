# Random health value for player
# Video 4 in playlist

import random

health = random.randint(10, 50)

def start_room(health):
    print('You have been attacked!')
    health -= 5
    print(f'You have {health} health points remaining!')

start_room(health)