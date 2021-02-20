"""
Create a Budget class that can instantiate objects based on
different budget categories like food, clothing, and entertainment.
These objects should allow for depositing and withdrawing funds from each category,
as well computing category balances and transferring balance amounts between categories

"""

# blueprint of the BUDGET APP

import colorama as color


class Budget:
    accounts = {'foodAccount': 0, 'clothingAccount': 0, 'entertainmentAcc': 0}

    def __init__(self, accName, accType, accNumber):
        self.accName = accName
        self.accType = accType
        self.accNumber = accNumber

    # returns nothing
    def deposit(self, amount):
        if self.accType == 'food':
            self.accounts['foodAccount'] += int(amount)
        elif self.accType == 'clothing':
            self.accounts['clothingAccount'] += int(amount)
        elif self.accType == 'entertainment':
            self.accounts['entertainmentAcc'] += int(amount)
        else:
            print(f'{color.Fore.RED} {self.accType} account is invalid! Please contact the support team.')

    # returns nothing
    def withdraw(self, amount):
        if self.accType == 'food':
            self.accounts['foodAccount'] -= int(amount)
        elif self.accType == 'clothing':
            self.accounts['clothingAccount'] -= int(amount)
        elif self.accType == 'entertainment':
            self.accounts['entertainmentAcc'] -= int(amount)
        else:
            print(f'{color.Fore.RED} {self.accType} account is invalid! Please contact the support team.')

    # returns the balance of each category
    def get_balance(self):
        if self.accType == 'food':
            return str(self.accounts['foodAccount'])
        elif self.accType == 'clothing':
            return str(self.accounts['clothingAccount'])
        elif self.accType == 'entertainment':
            return str(self.accounts['entertainmentAcc'])
        else:
            print(f'{color.Fore.RED} {self.accType} account is invalid! Please contact the support team.')

    # returns nothing
    def transfer_cash(self, amount, sender, receiver):
        if sender == 'food' and receiver != 'food':
            self.accounts['foodAccount'] -= int(amount)
            if receiver == 'clothing':
                self.accounts['clothingAccount'] += int(amount)
            elif receiver == 'entertainment':
                self.accounts['entertainmentAcc'] += int(amount)
            else:
                print(color.Fore.RED + 'Error! Try Again...')
        elif sender == 'clothing' and receiver != 'clothing':
            self.accounts['clothingAccount'] -= int(amount)
            if receiver == 'food':
                self.accounts['foodAccount'] += int(amount)
            elif receiver == 'entertainment':
                self.accounts['entertainmentAcc'] += int(amount)
            else:
                print(color.Fore.RED + 'Error! Try Again...')
        elif sender == 'entertainment' and receiver != 'entertainment':
            self.accounts['entertainmentAcc'] -= int(amount)
            if receiver == 'food':
                self.accounts['foodAccount'] += int(amount)
            elif receiver == 'clothing':
                self.accounts['clothingAccount'] += int(amount)
            else:
                print(color.Fore.RED + 'Error! Try Again...')
        else:
            print(color.Fore.RED + 'Error!!!')


if __name__ == '__main__':
    print(color.Fore.BLUE + 'Run the main.py file instead!')
