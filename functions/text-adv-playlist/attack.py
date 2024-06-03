# Attack function that passes an updated 
# health value to another function
# Video 5 in playlist

health = 20

def attack(health):
    health-= 5
    return health

def monster(health):
    print('You face a powerful dragon...and he viciously attacks you!')
    health = attack(health)
    print('As you flee the dragon, you suffer burns, so currently you')
    print(f'have {health} points remaining.')

monster(health)