accountName = ''
accountBalance = ''
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password
    
def show():
    global accountName, accountBalance, accountPassword
    print('    Name: ',accountName)
    print('    Balance: ',accountBalance)
    print('    Password: ', accountPassword)
    
def getBalance(password):
    global accountName, accountBalance, accountPassword
    if accountPassword == password:
        return accountBalance
    else:
        print('Incorrect password')
        return None

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('Cannot deposit a negative amount!')
        return None
    
    if accountPassword != password:
        print('Invalid password!')
        return None
    
    accountBalance = accountBalance + amountToDeposit
    return accountbalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    
    if accountBalance < amountToWithdraw:
        print('You exceed your account balance!')
        return None
    
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative number!')
        return None
    
    if accountPassword != password:
        print('Incorrect password!')
        return None
    
    accountBalance = accountBalance - amountToWithdraw
    return accountBalance



newAccount('Joe','100','soup')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()
    
    action = input('What do you want to do?')
    action = action.lower()
    action = action[0]
    print()
    
    if action == 'b':
        print()
        print('----Get Balance----')
        userPassword = input('What is the password?')
        theBalance = getBalance(userPassword)
        
        if theBalance is not None:
            print('Your balance is: ', theBalance)
        
    elif action == 'd':
        print()
        print('----Depositing to account----')
        userDeposit = input('Enter a balance.')
        userDeposit = int(userDeposit)
    
        userPassword = input('What is the password?')
        
        theDeposit = deposit(userDeposit, userPassword)
        
        if theDeposit is not None:
            print('Your new balance is $',theDeposit)
        
    
    elif action =='w':
        print()
        print('----Withdrawing from account----')
        userWithdraw = input('Enter the withdrawal amount.')
        userWithdraw = int(userWithdraw)
        
        userPassword = input('What is the password?')
        
        newBalance = withdraw(userWithdraw, userPassword)
        
        if newBalance is not None:
            print('Your new balance is $', newBalance)
    
            
    elif action == 's':
        print('--- Account Summary ----')
        print('Account:')
        show()
    
    elif action == 'q':
        break
        
    else:
        print('----Invalid command! Please try again----')
        print()


print('Thank you! See you again soon!')