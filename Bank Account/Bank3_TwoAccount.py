account0Name = ''
account0Balance = 0
account0Password = ''
account1Name = ''
account1Balance = 0
account1Password = ''
nAccounts = 0

def newAccount(accountNumber, name, balance, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        account0Name = name
        account0Balance = balance
        account0Password = password
        print('Account has been created!')
    
    if accountNumber == 1:
        account1Name = name
        account1Balance = balance
        account1Password = password
        print('Account has been created!')


def show():
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if account0Name != '':
        print('    Name: ',account0Name)
        print('    Balance: ',account0Balance)
        print('    Password: ', account0Password)

    if account1Name != '':
        print('    Name: ',account1Name)
        print('    Balance: ',account1Balance)
        print('    Password: ', account1Password)



def getBalance(accountNumber, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password
    if accountNumber == 0:
        if password != account0Password:
            print('Invalid password!')
            return None
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Invalid password!')
            return None
        return account1Balance


def deposit(accountNumber,amountToDeposit, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if password != account0Password:
            print('Invalid password!')
            return None
        
        if amountToDeposit < 0:
            print('Cannot deposit negative numbers!')
            return None
        
        account0Balance = account0Balance + amountToDeposit
        return account0Balance

    if accountNumber == 1:
        if password != account1Password:
            print('Invalid password!')
            return None
        
        if amountToDeposit < 0:
            print('Cannot deposit negative numbers!')
            return None
        
        account1Balance = account1Balance + amountToDeposit
        return account1Balance



def withdraw(accountNumber, amountToWithdraw, password):
    global account0Name, account0Balance, account0Password
    global account1Name, account1Balance, account1Password

    if accountNumber == 0:
        if account0Password != password:
            print('Invalid password!')
            return None
        if account0Balance < amountToWithdraw:
            print('Amount exceeds balance!')
            return None
        
        if amountToWithdraw < 0:
            print('Cannot withdraw negative numbers!')
            return None
        
        account0Balance = account0Balance - amountToWithdraw
        return account0Balance


    if accountNumber == 1:
        if account1Password != password:
            print('Invalid password!')
            return None
        if account1Balance < amountToWithdraw:
            print('Amount exceeds balance!')
            return None
        
        if amountToWithdraw < 0:
            print('Cannot withdraw negative numbers!')
            return None
        
        account1Balance = account1Balance - amountToWithdraw
        return account1Balance
    return None




newAccount(0,'Joe',100,'soup')
newAccount(1,'Sam',100,'soup')

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
        userAccountNumber = input('What is the account number?')
        userPassword = input('What is the password?')
        theBalance = getBalance(userAccountNumber, userPassword)
        
        if theBalance is not None:
            print('Your balance is: ', theBalance)
        
    elif action == 'd':
        print()
        print('----Depositing to account----')
        userDeposit = input('Enter a balance.')
        userDeposit = int(userDeposit)
    
        userAccount = input('What is the account number?')
        userPassword = input('What is the password?')
        
        theDeposit = deposit(userAccount, userDeposit, userPassword)
        
        if theDeposit is not None:
            print('Your new balance is $',theDeposit)
        
    
    elif action =='w':
        print()
        print('----Withdrawing from account----')
        userWithdraw = input('Enter the withdrawal amount.')
        userWithdraw = int(userWithdraw)
        
        userAccount = input('What is the account number?')
        userPassword = input('What is the password?')
        
        newBalance = withdraw(userAccount, userWithdraw, userPassword)
        
        if newBalance is not None:
            print('Your new balance is $', newBalance)
    
            
    elif action == 's':
        print('--- Account Summary ----')
        show()
    
    elif action == 'q':
        break
        
    else:
        print('----Invalid command! Please try again----')
        print()


print('Thank you! See you again soon!')