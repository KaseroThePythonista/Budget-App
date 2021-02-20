import time

import colorama as color

import module_budget as acc

import os

from colorama import init
init(autoreset=True)

print(color.Fore.BLUE + '                    BUDGET APP\n')
print(color.Fore.BLUE + ' To access any features of this app, Your details are required.\n')

# variables to inti the object of class Budget
print(color.Fore.GREEN + ' Account Name: ', end='')
account_name = input()
print(color.Fore.GREEN + ' Account number: ', end='')
account_number = input()


# function to describe all the available operation
def description():
    print(color.Fore.BLUE + '               WELCOME TO YOUR BUDGET ACCOUNT.')
    print(color.Fore.BLUE + 'SELECT AN OPERATION TO PERFORM: \n')
    print(color.Fore.BLUE + '     1. Deposit cash')
    print(color.Fore.BLUE + '     2. Withdraw cash')
    print(color.Fore.BLUE + '     3. Check balance')
    print(color.Fore.BLUE + '     4. Transfer funds')
    print(color.Fore.BLUE + '     5. EXIT\n')


while True:

    print()

    print(color.Fore.BLUE + 'Which Account would you like to access?\n')
    print(color.Fore.BLUE + '1. Food Account')
    print(color.Fore.BLUE + '2. Clothing Account')
    print(color.Fore.BLUE + '3. Entertainment Account')
    print(color.Fore.BLUE + '4. EXIT')

    # variable two, to init the object of class Budget
    print(color.Fore.GREEN + 'Type your selection here: ', end='')
    typeOfAccount = input()
    print()

    while True:

        if typeOfAccount == '1':
            accHolder = acc.Budget(account_name, 'food', account_number)

            print(color.Fore.YELLOW + '               FOOD ACCOUNT')
            description()

            print(color.Fore.GREEN + 'Type your selection here: ', end='')
            operation = input()

            if operation == '1':
                print('Enter the amount you wish to deposit: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.deposit(amount)
                os.system('cls')
                print(color.Fore.RED + 'Deposited Successfully.')
            elif operation == '2':
                print('Enter the amount you wish to withdraw: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.withdraw(amount)
                os.system('cls')
                print(color.Fore.RED + 'Withdrawn Successfully.')
            elif operation == '3':
                os.system('cls')
                print(f'{color.Fore.RED} Your Food Account balance is: {accHolder.get_balance()}')
            elif operation == '4':
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                print(color.Fore.GREEN + 'Sender(food, clothing, entertainment): ', end='')
                sender = input()
                print(color.Fore.GREEN + 'Receiver(food, clothing, entertainment)', end='')
                receiver = input()
                accHolder.transfer_cash(amount, sender, receiver)
                os.system('cls')
                print(color.Fore.RED + 'Transfer Successfully.')
            elif operation == '5':
                os.system('cls')
                break
            else:
                os.system('cls')
                print(color.Fore.RED + 'Wrong Selection!!!')

        elif typeOfAccount == '2':
            accHolder = acc.Budget(account_name, 'clothing', account_number)

            print(color.Fore.YELLOW + '               CLOTHING ACCOUNT')
            description()

            print(color.Fore.GREEN + 'Type your selection here: ', end='')
            operation = input()

            if operation == '1':
                print('Enter the amount you wish to deposit: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.deposit(amount)
                os.system('cls')
                print(color.Fore.RED + 'Deposited Successfully.')
            elif operation == '2':
                print('Enter the amount you wish to withdraw: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.withdraw(amount)
                os.system('cls')
                print(color.Fore.RED + 'Withdrawn Successfully.')
            elif operation == '3':
                print(f'{color.Fore.RED} Your Clothing Account balance is: {accHolder.get_balance()}')
            elif operation == '4':
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                print(color.Fore.GREEN + 'Sender(food, clothing, entertainment): ', end='')
                sender = input()
                print(color.Fore.GREEN + 'Receiver(food, clothing, entertainment)', end='')
                receiver = input()
                accHolder.transfer_cash(amount, sender, receiver)
                os.system('cls')
                print(color.Fore.RED + 'Transfer Successfully.')
            elif operation == '5':
                os.system('cls')
                break
            else:
                os.system('cls')
                print(color.Fore.RED + 'Wrong Selection!!!')

        elif typeOfAccount == '3':
            accHolder = acc.Budget(account_name, 'entertainment', account_number)

            print(color.Fore.YELLOW + '               ENTERTAINMENT ACCOUNT')
            description()

            operation = input(color.Fore.GREEN + 'Type your selection here: ')

            if operation == '1':
                print('Enter the amount you wish to deposit: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.deposit(amount)
                os.system('cls')
                print(color.Fore.RED + 'Deposited Successfully.')
            elif operation == '2':
                print('Enter the amount you wish to withdraw: ')
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                accHolder.withdraw(amount)
                os.system('cls')
                print(color.Fore.RED + 'Withdrawn Successfully.')
            elif operation == '3':
                print(f'{color.Fore.RED} Your Entertainment Account balance is: {accHolder.get_balance()}')
            elif operation == '4':
                print(color.Fore.GREEN + 'Amount: ', end='')
                amount = input()
                print(color.Fore.GREEN + 'Sender(food, clothing, entertainment): ', end='')
                sender = input()
                print(color.Fore.GREEN + 'Receiver(food, clothing, entertainment)', end='')
                receiver = input()
                accHolder.transfer_cash(amount, sender, receiver)
                os.system('cls')
                print(color.Fore.RED + 'Transfer Successfully.')
            elif operation == '5':
                os.system('cls')
                break
            else:
                os.system('cls')
                print(color.Fore.RED + 'Wrong Selection!!!')

        elif typeOfAccount == '4':
            os.system('cls')
            print(color.Fore.YELLOW + 'Shutting down the program in three(3) seconds!!!')
            print(color.Fore.YELLOW + 'Please wait....')
            time.sleep(3)
            exit()
