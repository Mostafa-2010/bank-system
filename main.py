from functions import *
import os
import json
import time

accounts = {}
developer_passcode = 'devpassonly7'  # For dev options and commands only

if os.path.exists('data.json') and os.path.getsize('data.json') > 0:
    try:
        with open('data.json', 'r') as f:
            accounts = json.load(f)
    except Exception:
        acounts = {}
            
menu_commands = ['create', 'find','delete', 'close']
in_account_commands = ['deposit', 'withdraw', 'transactions', 'change passcode', 'clear transactions', 'exit']        


while True:
    command = input(f"♦ Enter a command {menu_commands}: ").lower().strip()
    if command in menu_commands or command == 'clear data' or command == 'show data':
        if command == 'create':
            name_f = input('    ♦ Enter Your first name: ').lower().strip()
            name_l = input('    ♦ Enter your last name: ').lower().strip()
            try:
                passcode = int(input('    ♦ Enter a 6 digit passcode (only numbers): '))
                passcode_confirm = int(input('    ♦ Confirm the passcode again: '))
            except ValueError:
                print('♦ The passcode should be the number!')
                time.sleep(2)
            account_name = name_f + ' ' + name_l
            check = check_data(accounts, name_f, name_l, passcode, passcode_confirm,account_name )
            if check == 'valid':
                 add_account(accounts, name_f, name_l, passcode)
                 print('♦ Your account has been saved successfully!')
                 seperate()
                 time.sleep(2)
                
            else:
                print(check, "\n• Please try again!") 
                seperate()
                time.sleep(2)                
        elif command == 'find':
            account_name = input('    ♦ Enter the account name you want to find: ')
            if account_name in accounts:
                try:
                    passcode_check = int(input('    ♦ Enter the account passcode: '))
                except ValueError:
                    print('♦ The passcode must be a number')
                    seperate()
                    time.sleep(2)
                    
                if passcode_check == accounts[account_name]['passcode']:
                    seperate()
                    print(f"○ {account_name.upper()}: \n•    Balance: {accounts[account_name]['balance']}\n")
                    time.sleep(2)
                    seperate()
                    time.sleep(2)
                    
                    while True:      #in account actions
                        account_command = input(f"♦ Enter an operation: {in_account_commands} or 'exit' account: ").lower().strip()
                        if account_command in in_account_commands:
                            if account_command == 'exit':
                                break;
                            
                            elif account_command == 'transactions':
                                seperate()
                                time.sleep(2)
                                print('♦ Transactions history:')
                                for transaction in accounts[account_name]['transactions']:
                                    if transaction < 0:
                                        print(f'    ○ {transaction}$')
                                        time.sleep(1)
                                    elif transaction > 0:
                                        print(f'    ○ +{transaction}$')
                                        time.sleep(1)
                                seperate()      
                                time.sleep(3)
                            elif account_command == 'clear transactions':
                                insurance = input('♦ Are you sure you want to delete the transactions history Y/N: ').lower().strip()
                                if insurance == 'y':
                                    accounts[account_name]['transactions'] = []
                                    save(accounts)
                                    print('♠ The transactions history has been cleared!')
                                    seperate()
                                    time.sleep(2)
                            elif account_command == 'change passcode':
                                try:
                                    insure_passcode = int(input('♦ Enter you current password: '))
                                except ValueError:
                                    print('♦ Your passcode should be a number' )
                                    seperate()
                                    time.sleep(2)
                                if insure_passcode == accounts[account_name]['passcode']:
                                    try :
                                        new_passcode = int(input('♦ Enter your new passcode: '))
                                        confirm_new = int(input('♦ Confirm your new password: '))
                                    except ValueError:
                                        print('♦ The new passcode should be a number')
                                        seperate()
                                        time.sleep(2)
                                    if new_passcode == confirm_new:
                                        accounts[account_name]['passcode'] = new_passcode
                                        save(accounts)
                                        print('♦ your new passcode has been saved!')
                                        seperate()
                                        time.sleep(2)
                                    else:
                                        print('♦ Your passwords are not matched!, Please try again')
                                        seperate()
                                        time.sleep(2)
                            elif account_command == 'deposit' or account_command == 'withdraw':
                                if account_command == 'deposit':
                                        try :
                                            deposit = int(input('    ♦ Enter the amount for deposit: '))
                                            time.sleep(2)
                                        except ValueError:
                                            print('♦ The deposit amount should be a number!')
                                            seperate()
                                            time.sleep(2)
                                        if deposit > 10000:
                                            print( "♦ you can't deposit more than 10000$")
                                            seperate()
                                            time.sleep(2)
                                        elif deposit < 0:
                                            print('♦ The deposit can not be a negative number!')
                                            seperate()
                                            time.sleep(2)
                                        else:
                                            print('                    • Current Balance:',accounts[account_name]['balance'])
                                            deposit_and_withdraw(accounts, account_name, accounts[account_name]['balance'], accounts[account_name]['transactions'], deposit, 0, account_command)
                                            time.sleep(2)
                                            print('    ♦ Deposit added successfuly!')
                                            time.sleep(2)
                                            print(f"                    • Balance: {accounts[account_name]['balance']}$     (+ {deposit}$)")
                                            seperate()
                                            time.sleep(5)
                                        
                                elif account_command == 'withdraw':
                                    try :
                                        withdraw = int(input('    ♦ Enter the amount for withdrawal: '))
                                    except ValueError:
                                        print('♦ The withdrawal amount should be a number')
                                        seperate()
                                        time.sleep(2)
                                    if withdraw > accounts[account_name]['balance']:
                                        print( "♦ The amount of withdrawal in unavailable in your balance!")
                                        seperate()
                                        time.sleep(2)
                                    elif withdraw < 0:
                                        print('♦ Withdrawal can not be a negative number!')
                                        seperate()
                                        time.sleep(2)
                                    
                                    else:
                                        deposit_and_withdraw(accounts, account_name, accounts[account_name]['balance'], accounts[account_name]['transactions'], 0, withdraw, account_command )
                                        print('    ♦ withdrawal transacted successfuly!')
                                        time.sleep(2)
                                        print(f"    • Balance: {accounts[account_name]['balance']}$     (- {withdraw}$)")
                                        seperate()
                                        time.sleep(2)
                            else:
                                print('enter a valid command')
                                seperate()
                                time.sleep(2)
                        else:
                            print('enter a valid command')
                            seperate()
                            time.sleep(2)

                else:     
                    print('♦ Wrong passcode, check and try again')
                    seperate()
                    time.sleep(2)

            else:
                    print('♦ The account can not be found!')
                    seperate()
                    time.sleep(2)

        elif command == 'close':
            close()    
        elif command == 'clear data':
            dev_passcode = input('    ♦ Enter the dev passcode to clear the database: ')
            if dev_passcode == developer_passcode:
                insurance = input('    ♦ Are you sure to clear the databasse Y/N: ').lower().strip()
                time.sleep(1)
                if insurance == 'y':
                    clear(accounts)
                    print('♠ The Database has been cleared successfully!')
                    seperate()
                    time.sleep(4)
                    
                else:
                    print('♦ The deletion process has been cancelled!')
                    seperate()
                    time.sleep(2)
            else:
                print('♦ Wrong developer passcode!')
                seperate()
                time.sleep(2)
        elif command == 'delete':
            account_name = input('    ♦ Enter the account name you want to remover: ').lower().strip()
            print (account_name)
            if account_name in accounts:
                try:
                    check_passcode = int(input('    ♦ Enter the account passcode: '))
                except ValueError:
                    print('♦ The password should be a number!')
                    seperate()
                    time.sleep(2)
                if check_passcode == accounts[account_name]['passcode']:
                    insurance = input('    ♦ Are you sure you want to delete your account Y/N: ').lower().strip()
                    if insurance == 'y':
                        del accounts[account_name]
                        print('♦ YOUR ACCOUNT HAS BEEN DELETED!')
                        seperate()
                        time.sleep(2)
                    else:
                        print('♦ The deletion process has been cacelled!')
                        seperate()
                        time.sleep(2)
                else:
                    print('♦ This account can not be found!')
                    seperate()
                    time.sleep(2)
            else:
                print('♦ This account does not exist')
                seperate()
        elif command == 'show data':
                    dev_passcode = input('♦ Enter the dev passcode to show the database: ')
                    if dev_passcode == developer_passcode:
                            show(accounts)
                            seperate()
                            time.sleep(4)
                    
                    else:
                        print('♦ Wrong developer passcode!')
                        seperate()
                        time.sleep(2)
        else:
            print('♦ Please enter a valid command!')
            seperate()
            time.sleep(2)

    else:
        print('♦ Please enter a valid command create/find!')
        seperate()
