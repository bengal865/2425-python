# Slot Machine
# Source: https://youtu.be/f5J3YiZ3XX8?feature=shared

import emoji
import random

heart_emoji = emoji.emojize("\U0001F495")
banana_emoji = emoji.emojize('\U0001F34C')
pineapple_emoji = emoji.emojize('\U0001F34D')
apple_emoji = emoji.emojize('\U0001F34E')
watermelon_emoji = emoji.emojize('\U0001F349')
cherry_emoji = emoji.emojize('\U0001F352')
grapes_emoji = emoji.emojize('\U0001F347')
bell_emoji = emoji.emojize('\U0001F6CE')
christmas_tree_emoji = emoji.emojize('\U0001F384')

def spin_row():
    symbols = [cherry_emoji, watermelon_emoji, pineapple_emoji, bell_emoji, christmas_tree_emoji]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('**************')
    print('   '.join(row))
    print('**************')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == cherry_emoji:
            return bet * 3
        elif row[0] == watermelon_emoji:
            return bet * 4
        elif row[0] == pineapple_emoji:
            return bet * 5
        elif row[0] == bell_emoji:
            return bet * 10
        elif row[0] == christmas_tree_emoji:
            return bet * 20
    return 0 # If none of the symbols match, return zero

def main():
    balance = 100

    print('***********************')
    print('Welcome to Python Slots')
    print(f'Symbols: {cherry_emoji} {grapes_emoji} {watermelon_emoji} {christmas_tree_emoji} {bell_emoji}')
    print('***********************')

    while balance > 0:
        print(f'Current balance: ${balance}')

        bet = input('Place your bet amount:\n')

        if not bet.isdigit():
            print('Please enter numbers only!')
            continue

        bet = int(bet)

        if bet > balance:
            print('Insufficient funds! Your bet exceeds your balance!')
            continue

        if bet <= 0:
            print('Bets must be greater than zero!')
            continue

        balance -= bet

        row = spin_row() # Returns a list
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won ${payout}!')
        else:
            print('Sorry, you lost that round!')

        balance += payout

    # Play again?
        play_again = input('Do you want to spin again? (y/n)\n').lower()
        if play_again not in ['y', 'yes']:
            break

    print('**********************************************')
    print(f'Game over!  Your final balance is: ${balance}')
    print('**********************************************')


if __name__ == '__main__':
    main()