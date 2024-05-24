# Maze Game

import time

def maze():
    print('You are trying to find your way through a maze to the center')
    print('of the maze where there is a pot of gold!')
    print()
    time.sleep(2)
    print('What you don\'t realize is that the maze is a dangerous maze')
    print('full of traps and hazards.')
    print()
    time.sleep(2)
    print('Starting the maze game...')
    print()
    time.sleep(2)
    print('You enter the maze...')
    time.sleep(2)
    print('You can go (l)eft or (r)ight.')
    print()
    answer = input('Choose a direction! (l/r)').lower()
    print(f'You selected: {answer}')
    print('What will happen next?')
    time.sleep(2)
    print('You round the corner in the maze...')
    time.sleep(2)
    print('You walk forward a few steps...')
    time.sleep(2)
    if answer == 'r':
        print('...and fall down a trap door!')
        print('You are never seen again!')
    else:
        print('...and spy a beautiful grassy path lined with trees...')
        print('with a gigantic pot of gold at the end of the path!')


def main():
    maze()

main()