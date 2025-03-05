"""Defines the Bank class and is used by the BankingApplication module"""

import os
from AccountModule import Account, InvalidValue
from ChecquingAccountModule import ChecquingAccount
from SavingsAccountModule import SavingsAccount

class OperationCancel(Exception): 
    """Exception used when the user cancels an operation by pressing ENTER"""
    pass

class Bank:
    """
    Represents a bank composed of a list of accounts.

    Attributes:
        _accountList : list -- the list of accounts managed by the bank
    """

    def __init__(self):
        """Initialize the field variables of the bank object, the account of the bank"""
        self._accountList = []
        self.DEFAULT_ACCT_NO_START = 100        

    def loadAccountData(self):
        """Load the account data for all the accounts. The account data files are stored in a directory
        named BankingData located in the current directory, the directory used to run the application from
        """
        dataDirectory = os.path.join(os.getcwd(), 'BankingData')

        if os.path.exists(dataDirectory):
            #get the list of files in the directory
            acctFileList = os.listdir(dataDirectory)

            #go through the list of files, create the appropriate accounts and load the file
            for acctFileName in acctFileList:
                acctFile = open(os.path.join(dataDirectory,acctFileName))
                
                try:
                    #read the account type and create the correct account
                    acctType = acctFile.readline().rstrip('\n')
                    if acctType == 'Account':
                        acct = Account()
                    elif acctType == 'ChecquingAccount':
                        acct = ChecquingAccount()
                    elif acctType == 'SavingsAccount':
                        acct = SavingsAccount()

                    #load the data into the account object
                    acct.load(acctFile)

                    #add the account to the list of accounts
                    self._accountList.append(acct)

                finally:
                    #close the file regardless of whether an excetion occurrs or not the finally block will execute
                    #ensuring the file is closed. Alternatively the "with" statement could be used (see saveAccountData)
                    acctFile.close()
        
        #if at this point the list of accounts is empty add the defaults accounts so the application is usable
        if len(self._accountList) == 0:                    
            self.createDefaultAccounts()

    def saveAccountData(self):
        """Saves the data for all accounts in the data directory of the application. Each account is
        saved in a separate file which contains all the account information. The account data files are stored in a 
        directory named BankingData located in the current directory, the directory used to run the application from"""
        dataDirectory = os.path.join(os.getcwd(), 'BankingData')

        #make the directory if it does not exist
        if not os.path.exists(dataDirectory):
            os.mkdir(dataDirectory)

        #go through each account in the list of accounts and ask it to save itself into a corresponding file
        for acct in self._accountList:
            acctType = type(acct).__name__
            prefix = 'acct' if acctType == 'Account' else 'chqacct' if acctType == 'ChecquingAccount' else 'savacct'
            acctFileName = '{0}{1}.dat'.format(prefix, acct.getAccountNumber())
            
            #by using context manager for the file that will automatically close the file at the end of the with eblock
            with open(os.path.join(dataDirectory, acctFileName), 'w') as acctFile:
                acctFile.write(acctType + '\n')
                acct.save(acctFile)

    def createDefaultAccounts(self):
        """Create 10 accounts with predefined IDs and balances. The default accounts are created only
        if no account data files exist"""

        for iAccount in range(10):
            #create the account with required properties
            newDefAcct =  Account(self.DEFAULT_ACCT_NO_START + iAccount, 
                                  "DefaultAccount{0}".format(iAccount))
            newDefAcct.deposit(100)
            newDefAcct.setAnnualIntrRate(2.5)

            #add the account to the list
            self._accountList.append(newDefAcct)


    def findAccount(self, acctNo):
        """
        Returns the account with the given account number or null if no account with that ID can be found
        Parameters:
            acctNo - the account number of the account to return
        Return:
            the account object with the given ID
        """
        #go through all the accounts until one is found with the given account number
        for acct in self._accountList:
            if acct.getAccountNumber() == acctNo:
                return acct

        #if the program got here it means there was no account with the given account number
        return None


    def determineAccountNumber(self):
        """Determine the account number prompting the user until they enter the correct information
        
           The method will raise an AssertError if the user chooses to terminate.
        """
        #pylint: disable=no-self-use
        while True:
            try:
                #ask the user for input
                acctNoInput = input('Please enter the account number [100 - 1000] or press [ENTER] to cancel: ')

                if len(acctNoInput) == 0:
                    raise OperationCancel('User has selected to terminate the program after invalid input')

                #check the input to ensure correctness and deal with incorrect input
                acctNo = int(acctNoInput)
                if acctNo < 100 or acctNo > 1000: 
                    raise InvalidValue('The account number you have entered is not valid. Please enter a valid account number')

                #check that the account number is not in use
                for account in self._accountList:
                    if acctNo == account.getAccountNumber():
                        raise InvalidValue('The account number you have entered already exists. Please enter a different account number')
                
                #the account number has been generated successfully
                return acctNo

            except (ValueError, InvalidValue) as err:
                print(err, '\n') 

    def openAccount(self, clientName, acctType):
        """Create and store an account objec with the required attributes"""
        #prompt the user for an account number
        acctNo = self.determineAccountNumber()
        
        #create and store an account object with the required attributes
        if acctType == Account.ACCOUNT_TYPE_CHECQUING:
            newAccount = ChecquingAccount(acctNo, clientName)
        elif acctType == Account.ACCOUNT_TYPE_SAVINGS:
            newAccount = SavingsAccount(acctNo, clientName)

        #add the new account to the list of the accounts
        self._accountList.append(newAccount)

        #return the account to the caller so other properties can be set
        return newAccount

