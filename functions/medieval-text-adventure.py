# Medieval Text Adventure
# 18 MAY 20XX

import time

delay = 0.75 # Delay in seconds

def welcome():
    print('You are a medieval knight who is out exploring the local area.')
    time.sleep(delay)
    print('You approach a castle, and as you near the main gate, you suddenly hear some shouting')
    print('on the wall of the castle that overlooks your position.')
    time.sleep(delay)
    print('It appears the lord of the castle has decided you are trespassing on his land, and')
    print('has ordered his men to prepare to attack you and your men.')
    time.sleep(delay)
    print('You must quickly make a decision before the castle\'s defenders launch their attack...')
    time.sleep(delay)
    print('Do you [d]ive into the moat or temporarily [r]etreat to the safety of the thick woods surrounding the castle? (Enter \'d\' for dive, \'r\' for retreat))')

    choice = input('').lower()
    if choice == 'd':
        dive()
    elif choice == 'r':
        retreat()
    else:
        invalid_choice()
        welcome()


def stable():
    pass


def higher_ground():
    pass


def dive():
    print('''You dive into the moat and attempt to swim to safety.  Your armor, though, is too heavy, and you find yourself slipping deeper and deeper into the moat.
          Struggling, your lungs fill with water and you drown at the bottom of the moat, never to see your companions and loved ones again.''')
    choice = input('Would you like to play again? (y/n)').lower()
    if choice == 'y' or choice == 'yes':
        welcome()
    else:
        print('Thanks for playing!')
        time.sleep(delay)
        print('Good day!')

def retreat():
    print('''You see the defenders starting to draw their bows.  You sprint across the open field that separates the castle from the woods.  The defenders
          loose their arrows, and while you are running, you can hear the arrows whizzing over your head and striking the ground around you.  In the nick of time,
          you and your men reach the forest and hastily take cover behind tree trunks and a rocky outcrop located just inside the edge of the forest.''')
    time.sleep(delay)
    print('''You call over your second-in-command and take two minutes to discuss how to respond to the attack just launched against you. To the left of the
          castle you see a large stable that appears to be unguarded.  To the right of the castle is higher ground that offers an unrestricted view of
          the castle's interior defenses and more protection than the forest you and your men are currently hiding in.''')
    time.sleep(delay)
    print('What will be your next move?')
    time.sleep(delay)
    print('Will you flank the castle defenders and move to the nearby [s]table or seek a better vantage point in the higher [g]round to the right of the castle?')
    time.sleep(delay)
    print('Enter s to move to the [s]table or g to move to higher [g]round...')
    choice = input().lower()
    if choice == 's':
        stable()
    elif choice == 'g':
        higher_ground()
    else:
        invalid_choice()

def invalid_choice():
    print('Invalid entry! Please try again!')

# Call the welcome function to start the text adventure
welcome()