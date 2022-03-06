accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print()
    print('---- Menu ----')
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show account')
    print('Press q to quit')
    print()
    
    action = input('What would you like to do? ')
    
    if action == 'b':
        print()
        print('----Get Balance----')
        userPassword = input('What is the password?')
        if userPassword != accountPassword:
            print('You entered the wrong password!')
        else:
            print('The balance of your account is: ', accountBalance)
        
    elif action == 'd':
        print()
        print('----Depositing to account----')
        userDeposit = input('Enter a balance.')
        userDeposit = int(userDeposit)
    
        userPassword = input('What is the password?')
    
        if userDeposit < 0:
            print('You cannot deposit a negative balance!')
        elif userPassword != accountPassword:
            print('You entered the wrong password!')
        else:
            accountBalance = accountBalance + userDeposit
            print('Your new balance is ', accountBalanace)
    
    elif action =='w':
        print()
        print('----Withdrawing from account----')
        userWithdraw = input('Enter the withdrawal amount.')
        userWithdraw = int(userWithdraw)
        
        userPassword = input('What is the password?')
    
        if userWithdraw < 0:
            print('----You cannot withdraw a negative balance!----')
        elif userWithdraw > accountBalance:
            print('----You do not have enough cash in your account.')
        elif userPassword != accountPassword:
            print('You entered the wrong password!')
        else:
            accountBalance = accountBalance - userWithdraw
            print('Your new balance is ', accountBalanace)
            
    elif action == 's':
        print('--- Account Summary ----')
        print('Account:')
        print('        Name: ', accountName)
        print('        Balance: ', accountBalance)
        print('        Password: ', accountPassword)
    
    elif action == 'q':
        break
        
    else:
        print('----Invalid command! Please try again----')
        print()


print('Thank you! See you again soon!')