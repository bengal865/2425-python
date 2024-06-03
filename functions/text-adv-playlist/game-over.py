health = 20

def attack(health):
    health-= 5
    return health

def monster(health):
    print('You face a powerful dragon...and he viciously attacks you!')
    health = attack(health)
    print('As you flee the dragon, you suffer burns, so currently you')
    print(f'have {health} points remaining.')

    if health < 1:
        game_over()
    print('Do you wish to launch another attack? (y/n)')
    answer = input().lower()
    if answer == 'yes' or answer == 'y':
        monster(health)
    else:
        print('You run away from the dragon.')

def game_over():
    print('The light fades from your eyes as you slip into eternal darkness.')
    quit()

monster(health)