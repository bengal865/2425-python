# Text Adventure Game
# Part 3 video

# Source: https://youtube.com/playlist?list=PLES3Y8j562C2ncjly27QLCz3TWuFlzKVq&feature=shared

import time
delay = 0.75

# Create a list to store the items found in the game
inventory = ['knife', 'cheese']

def start_room():
    print('You are in a hall.')
    time.sleep(delay)
    print('You see a gold coin on the floor.')
    time.sleep(delay)
    print('Do you pick up the coin? (y/n)')
    grab_coin = input().lower()
    if grab_coin in ['y', 'yes']:
        add_to_inventory('coin')
    else:
        print('You left the gold coin on the floor.')
    second_room()

def second_room():
    print('You arrive at a dark, winding river, where there is a ferry.')
    time.sleep(delay)
    print('Do you wish to see if you have anything in your inventory')
    print('you could give the ferryman to convince him to take you across the river? (y/n)')
    check_inventory = input().lower()
    if check_inventory in ['y', 'yes']:
        print_inventory()
    else:
        # If the player didn't pick up the gold coin, it won't be in the inventory, so player
        # can't board the ferry and cross the river
        if 'coin' not in inventory:
            print('You have nothing to offer the ferryman, so he refuses you passage across the river!')
        else:
            print('The ferryman accepts your gold coin and invites you to board his ferry.')


def add_to_inventory(item):
    inventory.append(item)

def print_inventory():
    for item in inventory:
        print(item)
    second_room()

start_room()
