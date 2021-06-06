import os
import random
import datetime

database = {}

def init():

    print('Welcome to Bank of Burien')


    haveAccount = int(input('Do you have an account with us?: \n 1 (yes) 2 (no) \n'))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()
    else:
        print('You have selected an invalid option')
        init()

def login():
    readUserData()
    now = datetime.datetime.now()
    print(now.strftime('%b %d, %Y %I:%M %p'))
    print('***** Please login to your account *****')

    accountNumberFromUser = int(input('What is your account number \n'))
    password = input('Please enter your password \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                authSession(accountNumber)
                print('Welcome %s %s' % (database[accountNumber][0], database[accountNumber][1]))
                bankOperation(accountNumber)
        
    print('Invalid account or password, Please try again')
    login()

def register():
    now = datetime.datetime.now()
    print(now.strftime('%b %d, %Y %I:%M %p'))

    print('***** Please Register to create an Account *****')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a password \n')

    accountNumber = generateAccountNumber()
    accountBalance = 0

    database[accountNumber] = [ first_name, last_name, email, password, accountBalance ]
    
    print('your account has been created')
    print('you account number is %d' %accountNumber)
    print('Please keep this for your records')

    saveUserData()
    login()

def bankOperation(accountNumber):
    saveUserData()

    selectedoption = int(input('What would you like to do? \n (0) Check Balance (1) Deposit \n (2) Withdraw (3) Logout \n (4) Report an Issue (5)Exit \n'))
    if(selectedoption == 0):
        print('Your Balance is %s' %database[accountNumber][4])
        bankOperation(accountNumber)
    elif(selectedoption == 1):
        depositOperation(accountNumber)
    elif(selectedoption == 2):
        withdrawalOperation(accountNumber)
    elif(selectedoption == 3):
        os.remove("session.txt")
        login()
    elif(selectedoption == 4):
        issues = input('Please report any issues you have come across \n')
        print('Thank you for your feedback, we will contact if needed \n')
        bankOperation(accountNumber)
    elif(selectedoption == 5):
        exit()
    else:
        print('Invalid option selected')
        bankOperation(accountNumber)

def withdrawalOperation(accountNumber):

    print('**** withdrawal ****')
    withdrawalAmount = int(input('How much would you like to withdraw? \n'))
    if(0 < withdrawalAmount <= 500):
        database[accountNumber][4] -= withdrawalAmount

        print('Please take your %s' %withdrawalAmount)
        print('Your balance is now $%s' %database[accountNumber][4])
        bankOperation(accountNumber)
    elif(withdrawalAmount <= 0):
        print('Please withdraw atleast $1')
        withdrawalOperation(accountNumber)
    elif(withdrawalAmount > 500):
        print('You may not withdraw more than $500 per transaction, please try again')
        withdrawalOperation(accountNumber)

def depositOperation(accountNumber):
    print('**** Deposit ****')
    depositAmount = int(input('How much would you like to deposit? \n'))
    if(0 < depositAmount <= 5000):
        database[accountNumber][4] += depositAmount
        print('You have deposited $%s' %depositAmount)
        print('Your balance is now $%s' %database[accountNumber][4])
        bankOperation(accountNumber)
    elif(depositAmount <= 0):
        print('Invalid amount, Please deposit at least $1')
        depositOperation(accountNumber)
    elif(depositAmount > 5000):
        print('You may not deposit more than $5000 per transaction, please try again')
        depositOperation(accountNumber)

def generateAccountNumber(): 

    print('Generating Account Number')
    return random.randrange(1111111111,9999999999)

def saveUserData():
    global database
    f = open("BBDatabase.txt", "w")
    f.write(str(database))
    f.close()
    
def readUserData():
    global database
    f=open('BBDatabase.txt', 'r')
    ts = f.read()
    f.close()
    database = eval(ts)

def authSession(accountNumber):
    a=open("session.txt", "w")
    a.write(str(accountNumber))
    a.close()






readUserData()
init()


