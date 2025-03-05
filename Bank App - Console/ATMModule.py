from AccountModule import Account, InvalidValue
from AccountModule import InvalidTransaction
from BankModule import OperationCancel
from ChecquingAccountModule import ChecquingAccount
from SavingsAccountModule import SavingsAccount

class Atm:
    """ 
    The Atm class representing an ATM machine. The class displays and performs the the account management functions
    on a given bank account: checking balance, withdrawing and depositing money
    Magdin Stoica
    
    Version 3.0 (Python)
    """
    def __init__(self, bank):

        #the bank this ATM object is working with
        self._bank = bank

        #create the MAIN MENU options
        self.SELECT_ACCOUNT_OPTION = 1
        self.CREATE_ACCOUNT_OPTION = 2
        self.EXIT_ATM_APPLICATION_OPTION = 3

        #create ACCOUNT MENU option
        self.CHECK_BALANCE_OPTION = 1
        self.WITHDRAW_OPTION = 2
        self.DEPOSIT_OPTION = 3
        self.EXIT_ACCOUNT_OPTION = 4
    
    def start(self):
        """
        Starts the ATM program by displaying the required user options. 
        User navigates the menus managing their accounts
        """
        #keep displaying the menu until the user chooses to exit the application
        while True:
            #display the main menu and perform the main actions depending on the user's choice
            selectedOption = self.showMainMenu()

            if selectedOption == self.SELECT_ACCOUNT_OPTION:
                acct = self.selectAccount()
                if acct != None:
                    self.manageAccount(acct)
            elif selectedOption == self.CREATE_ACCOUNT_OPTION:
                self.onCreateAccount()
            elif selectedOption == self.EXIT_ATM_APPLICATION_OPTION:
                #the application is shutting down, save all account information
                self._bank.saveAccountData()
                return
            else:
                #go again when the user choose 3 instead of 1 or 2
                print('Please enter a valid menu option', "\n")

    def showMainMenu(self):
        """
        Displays the main ATM menu and ensure the user picks an option. Handles invalid input but doesn't check
        that the menu option is one of the displayed ones.
        Returns:
            the option selected by the user

        """
        while True:
            try:
                return int(input('\nMain Menu\n\n1: Select Account\n2: Create Account\n3: Exit\n\nEnter a choice: ')) 
            except ValueError:
                #if the user enters "abc" instead of a number
                print("Please enter a valid menu option.", "\n");

    def showAccountMenu(self):
        """
        Displays the ACCOUNT menu that allows the user to perform account operations. Handles invalid input but doesn't check
        that the menu option is one of the displayed ones.
        Returns:
            the option selected by the user
        """
        while True:
            try:
                return int(input('\nAccount Menu\n\n1: Check Balance\n2: Withdraw\n3: Deposit\n4: Exit\n\nEnter a choice: ')) 
            except ValueError:
                #if the user enters "abc" instead of a number
                print("Please enter a valid menu option.", "\n");

    def onCreateAccount(self):
        """Create and open an account. The user is prompted for all account information including the type of account to open.
        Create the account object and add it to the bank
        """
        while True:
            try:
                #get the name of the account holder from the user
                clientName = self.promptForClientName()

                #get the initial deposit from the user
                initDepositAmount = self.promptForDepositAmount()

                #get the annual interest rate from the user
                annIntrRate = self.promptForAnnualIntrRate()

                #get the account type from the user
                acctType = self.promptForAccountType()
        
                #open the account
                newAccount = self._bank.openAccount(clientName, acctType)        

                #set the other account propertites
                newAccount.deposit(initDepositAmount)
                newAccount.setAnnualIntrRate(annIntrRate)

                #now the the account has been successfully created and added to the bank the method is done
                return
                            
            except InvalidValue as err:
                print(err, "\n")

            except OperationCancel as err:
                print(err, "\n")
                return #the user has canceled the creation of the account           

    def selectAccount(self):
        """Select an account by prompting the user for an account number and remembering which account was selected.
        Prompt the user for performing account information such deposit and withdrawals
        """

        while True:
            try:
                acctNoInput = input('Please enter your account ID or press [ENTER] to cancel: ')
                
                #check to see if the user gave up and is canceling the operation                
                if len(acctNoInput) == 0:
                    return None

                #the user entered an account number get the actual number
                acctNo = int(acctNoInput)

                #obtain the account required by the user from the bank
                acct = self._bank.findAccount(acctNo)
                if acct != None:
                    return acct
                else:
                    print('The account was not found. Please select another account.')
            except ValueError:
                #The user entered an invalid (e.g. abc) account ID
                print('Please enter a valid account number (e.g. 100)', "\n")

    def manageAccount(self, account):
        """Manage the account by allowing the user to execute operation on the given account
        Arguments:
            account - the account to be managed
        """

        while True:
            selAcctMenuOpt = self.showAccountMenu()

            if selAcctMenuOpt == self.CHECK_BALANCE_OPTION:
                self.onCheckBalance(account)
            elif selAcctMenuOpt == self.WITHDRAW_OPTION:
                self.onWithdraw(account)
            elif selAcctMenuOpt == self.DEPOSIT_OPTION:
                self.onDeposit(account)
            elif selAcctMenuOpt == self.EXIT_ACCOUNT_OPTION:
                return
            else:
                print('Please enter a valid menu option')

    def promptForClientName(self):
        """Prompts the user to enter the name of the client and allows the user to cancel by pressing ENTER"""
        clientName = input('Please enter the client name or press [ENTER] to cancel: ')
        
        if len(clientName) == 0:
            #the user has canceled the creation of the account
            raise OperationCancel('The user has selected to cancel the current operation')
        
        return clientName

    def promptForDepositAmount(self):
        """Prompts the user to enter an account balance and performs basic error checking"""
        while True:
            try:
                initAmount = float(input('Please enter your initial account balance: '))

                if initAmount >= 0:
                    return initAmount
                else:
                    #NOTE the difference between this error which is handled with an if statement
                    #and the ValueError exception. In this case an if statement is more suitable because
                    #it makes the code more readable than a try/catch.
                    print('Cannot create an account with a negative initial balance. Please enter a valid amount')
            except ValueError as err:
                print(err, "\n")

    def promptForAnnualIntrRate(self):
        """Prompts the user to enter the annual interest rate for an account"""
        while True:
            try:
                intrRate = float(input('Please enter the interest rate for this account: '))

                #perform basic sanity checking of the input. Note that the business rules for checking are implemented
                #in the account classes not here so that they are together with the rest of the account business logic
                if intrRate >= 0:
                    return intrRate
                else:
                    #NOTE the difference between this error which is handled with an if statement
                    #and the ValueError exception. In this case an if statement is more suitable because
                    #it makes the code more readable than a try/catch.
                    print('Cannot create an account with a negative interest rate.')
            except ValueError as err:
                print(err, "\n")

    def promptForAccountType(self):
        """Prompts the user to enter an account type
        Returns:
            - the account type as a constant
        """
        while True:
            acctTypeInput = input('Please enter the account type [c/s: chequing / savings]: ').upper()
            if acctTypeInput == 'C' or acctTypeInput == 'CHECQUING' or acctTypeInput == 'CHECKING':
                return Account.ACCOUNT_TYPE_CHECQUING
            elif acctTypeInput == 'S' or acctTypeInput == 'SAVINGS' or acctTypeInput == 'SAVING':
                return Account.ACCOUNT_TYPE_SAVINGS
            else:
                print('Answer not supported. Please enter one of the supported answers.')

    def onCheckBalance(self, account):
        """
        Prints the balance in the given account
        Arguments:
            account - the account for which the balance is printed  
        """
        print('The balance is {0}\n'.format(account.getBalance()))

    def onDeposit(self, account):
        """
        Prompts the user for an amount and performs the deposit. Handles any errors related to incorrect amounts
        Arguments:
            account - the account in which the amount is to be deposited
            
        """
        while True:
            try:
                inputAmount = input('Please enter an amount to deposit or type [ENTER] to exit: ')
                
                #test for empty input in case the user pressed [ENTER] because they wanted to give up on depositing money
                if len(inputAmount) > 0:
                    amount = float(inputAmount)
                
                    #the account itself is responsible for checking the amount and raising any errors if the deposit
                    #is not possible like negative amounts 
                    account.deposit(amount)
                
                #the deposit was done or user entered nothing so break from the infinite loop
                return

            except ValueError:
                #the user must have entered and invalid (e.g. "abc") amount
                print('Invalid entry. Please enter a number for your amount.', "\n")

            except InvalidTransaction as err:
                #the account must have refused to deposit the entered amount. The reason is in the exception object
                print(err, "\n")


    def onWithdraw(self, account):
        """
        Prompts the user for an amount and performs the withdrawal. Handles any errors related to incorrect amounts
        Arguments:
            account - the account in which the amount is to be withdrawn
            
        """
        while True:
            try:
                inputAmount = input('Please enter an amount to withdraw or type [ENTER] to exit: ')
                
                #test for empty input in case the user pressed [ENTER] because they wanted to give up on withdrawing money
                if len(inputAmount) > 0:
                    amount = float(inputAmount)
                
                    #the account itself is responsible for checking the amount and raising any errors if the withdraw
                    #is not possible like negative amounts and balance overruns
                    account.withdraw(amount)
                
                #the deposit was done or user entered nothing so break from the infinite loop
                return

            except ValueError:
                #the user must have entered and invalid (e.g. "abc") amount
                print('Invalid entry. Please enter a number for your amount.', "\n")

            except InvalidTransaction as err:
                #the account must have refused to withdraw the entered amount. The reason is in the exception object
                print(err, "\n")
    