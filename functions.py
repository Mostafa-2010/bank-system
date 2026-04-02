# Functions file that is imported in the main program file.

import sys
import json
import time

def save(accounts):
    with open('data.json', 'w') as f:
        json.dump(accounts, f, indent=4)
        
def seperate():   # Format function
    print('∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙∙')
    

def check_data(accounts, name_f, name_l, password, password_confirm, account_name):       # security and verfication function
    if name_f == '' or name_l == '':
        return '♦ First and last name should not be empty!'

    elif not len(name_f) in range(2, 12) or not len(name_l) in range(2, 12):
        return "♦ The name's charcters should be between 2 and 11 characters!"

    elif name_f.isdigit() or name_l.isdigit():
        return "♦ The names can't be a number!"

    elif ' ' in name_f or ' ' in name_l:
        return "♦ The names can't contain spaces"

    elif len(str(password)) != 6:
        return '♦ The passcode should be 6 numbers!'

    elif password != password_confirm:
        return '♦ The passwords you entered are not matched!'

    elif account_name in accounts:
        return '♦ This account already exists!'
        
    else:
        return 'valid'
        
def add_account(accounts, name_f, name_l, passcode):
    account_name = name_f + ' ' + name_l
    accounts[account_name] = {
        'balance':0,
        'passcode':passcode,
        'transactions':[]}
    save(accounts)


def deposit_and_withdraw(accounts, account_name, balance, transactions, deposit, withdraw, command):
    if command == 'deposit':
        accounts[account_name]['balance'] += deposit
        accounts[account_name]['transactions'].append(deposit)
        save(accounts)
    elif command == 'withdraw':
        accounts[account_name]['balance'] -= withdraw
        accounts[account_name]['transactions'].append(-withdraw)
        save(accounts)

def clear(accounts):
    accounts.clear()
    save(accounts)
    
def close():
    print('--------------------------------closing the program--------------------------------'.center(120))
    time.sleep(8)
    sys.exit()

def show(accounts):
    for key, value in accounts.items():
        print(f'\n{key}:{value}\n')
        time.sleep(4)
