"""Defines the Account class and used by the BankingApplication module."""

class InvalidTransaction(Exception): 
    """Exception class used when an invalid trasaction is performed"""
    pass

class InvalidValue(Exception): 
    """Exception class used when an invalid value is detected"""
    pass

class Account:
    """
    Defines a bank account its associated attributes and operations.

    Attributes:
        _acctNo         : int   -- the account number, read-only attribute
        _acctHolderName : str   -- the name of the account holder, read-only attribute
        _balance        : float -- the account balance that gets affected by withdrawls and deposits
        _annualIntrRate : float -- the annual interest rate applicable on the balance
    """

    #these are class variables which are not specific to an instance, they are not field variables
    #they are shared by all instances and are accessible using the name of the class with the DOT notation
    """constant representing a checquing account type"""
    ACCOUNT_TYPE_CHECQUING = 1

    """constant representing a savings account type"""
    ACCOUNT_TYPE_SAVINGS = 2

    def __init__(self, acctNo=-1, acctHolderName=''):
        """
        Initialize the account object with its attributes.

        The account constructor requires the caller to supply an account number and
        the name of the account holder in order to create an account. 

        NOTE: the constructor assigns default values to each parameter allowing the code
        not to supply them (i.e. acct = Account()). If the calling code does not supply
        values for the two parameters they will receive these default values. This is used
        when the accounts are created from data files 
        
        Arguments:
            acctNo          : int   -- the account number, required parameter
            acctHolderName  : str   -- the name of the account holder, required parameter
        """
        self._acctNo = acctNo
        self._acctHolderName = acctHolderName
        self._balance = 0.0
        self._annualIntrRate = 0.0

    def getAccountNumber(self):
        """Return the account number."""
        return self._acctNo

    def getAcctHolderName(self):
        """Return the account holder's name"""
        return self._acctHolderName

    def getBalance(self):
        """Return the balance in the account"""
        return self._balance
    
    def getAnnualIntrRate(self):
        """Return the annuaul interest rate on the account"""
        return self._annualIntrRate

    def setAnnualIntrRate(self, newAnnualIntrRatePercentage):
        """
        Change the annual interest rate on the account

        Arguments:
            newAnnualIntrRatePercentage: float -- the annual interest as a percentage (e.g. 3%)
        """
        self._annualIntrRate = newAnnualIntrRatePercentage / 100

    def getMonthlyIntrRate(self):
        """Calculate and return the monthly interest rate on the account"""
        return self._annualIntrRate / 12

    def deposit(self, amount):
        """Deposit the given amount in the account and return the new balance
        Arguments:
            amount - the amount to be deposited
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """

        #check that the amount is positive
        if amount < 0:
            raise InvalidTransaction( 'Invalid amount provided. Cannot deposit a negative amount.')
        
        #change the balance
        oldBalance = self._balance
        self._balance += amount

        #provide the new balance to the caller to avoid a getBalance() call
        return self._balance

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account and return teh new balance
        Arguments:
            amount - the amount to be withdrawn, cannot be negative or greater than available balance             
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """
        #pylint: disable=no-self-use, unused-argument
        if amount < 0:
            raise InvalidTransaction('Invalid amount provided. Cannot withdraw a negative amount.')

        if amount > self._balance:
            raise InvalidTransaction('Insufficient funds. Cannot withdraw the provided amount.')

        #change the balance
        oldBalance = self._balance
        self._balance -= amount
        
        #provide the new balance to the caller to avoid a getBalance() call
        return self._balance

    def load(self, file):
        """Load the account information from the given file. The file is assumed opened
        Arguments:
            file - the file containing the account information
        """
        #read the account properties in the same order they were saved
        self._acctNo = int(file.readline().rstrip('\n'))
        self._acctHolderName = file.readline().rstrip('\n')
        self._balance = float(file.readline().rstrip('\n'))
        self._annualIntrRate = float(file.readline().rstrip('\n'))        

    def save(self, file):
        """Save the account information in the given file. The file is assumed opened
        Arguments:
            file - the file to contain the account information
        """
        #write the account properties, one per line
        file.write(str(self._acctNo) + '\n')
        file.write(str(self._acctHolderName) + '\n')
        file.write(str(self._balance) + '\n')
        file.write(str(self._annualIntrRate) + '\n')






