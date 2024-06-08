# Banking Project
# Source: https://youtu.be/8aW3tkIul-8?feature=shared

def show_balance(acct_balance):
    print('************************')
    print(f'Your balance is ${acct_balance:.2f}')
    print('************************')

def deposit():
    print('************************')
    amount = float(input('Enter an amount to be deposited:\n'))
    print('************************')
    if amount < 0:
        print('************************')
        print('Invalid amount! Amount must be greater than zero!')
        print('************************')
        return 0
    else:
        return amount

def withdraw(acct_balance):
    print('************************')
    amount = float(input('Enter amount to be withdrawn:\n'))
    print('************************')

    if amount > acct_balance:
        print('************************')
        print('Insufficient funds!')
        print('************************')
        return 0
    elif amount < 0:
        print('************************')
        print('Amount to withdraw must be greater than zero!')
        print('************************')
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True


    while is_running:
        print('**********************************')
        print('     Career Tech Banking Menu     ')
        print('**********************************')
        print('1. Show Balance')
        print('2. Make Deposit')
        print('3. Withdraw Cash')
        print('4. Exit\n')
        print('************************')
        choice = input('Enter a menu option (1 - 4)\n')
        print('************************')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('************************')
            print('Invalid menu selection!  Enter 1 - 4 only!')
            print('************************')

    print('************************************') 
    print('Thank you for using the Career Tech Banking app!')
    print('Please visit us again soon!')
    print('************************************')

if __name__ == '__main__':
    main()