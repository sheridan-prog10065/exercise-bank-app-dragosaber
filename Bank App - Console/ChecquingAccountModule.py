from AccountModule import Account, InvalidValue, InvalidTransaction

class ChecquingAccount(Account):
    """Represents a chequing account that has an overdraft limit and a maximum interest rate"""

    """The amount of overdraft is constant. Defined as a class variable and accessible
    through the name of the class along with the DOT notation"""
    OVERDRAFT_LIMIT = 500

    """The maximum interest rate for checquing accounts. Defined as a class variable and accessible
    through the name of the class along with the DOT notation """
    MAX_INTEREST_RATE = 1.0

    def __init__(self, acctNo=-1, acctHolderName=''):
        """Provide a constructor and ensure the base contstructor gets called

        NOTE: the constructor assigns default values to each parameter allowing the code
        not to supply them (i.e. acct = ChequingAccount()). If the calling code does not supply
        values for the two parameters they will receive these default values. This is used
        when the accounts are created from data files 

        Arguments:
            acctNo          : int   -- the account number, required parameter
            acctHolderName  : str   -- the name of the account holder, required parameter
        """
        Account.__init__(self, acctNo, acctHolderName)

    def setAnnualIntrRate(self, newAnnualIntrRatePercentage):
        """
        Change the annual interest rate on the account. Verify the annual interest rate is valid for a checquing account

        Arguments:
            newAnnualIntrRatePercentage: float -- the annual interest as a percentage (e.g. 3%)
        """
        #check to ensure the annual interest rate is valid for a checquing account
        if newAnnualIntrRatePercentage > ChecquingAccount.MAX_INTEREST_RATE:
            raise InvalidValue('A checquing account cannot have an interest rate greater than {0}'.format(ChecquingAccount.MAX_INTEREST_RATE))
        
        #use the base class to set the annual interest rate
        Account.setAnnualIntrRate(self, newAnnualIntrRatePercentage)

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account and return teh new balance
        Arguments:
            amount - the amount to be withdrawn, cannot be negative or greater than balance and overdraft combined            
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """
        #pylint: disable=no-self-use, unused-argument
        if amount < 0:
            raise InvalidTransaction('Invalid amount provided. Cannot withdraw a negative amount.')

        #check the overdraft on top of the actual balance
        if amount > self._balance + ChecquingAccount.OVERDRAFT_LIMIT:
            raise InvalidTransaction('Insufficient funds. Cannot withdraw the provided amount.')

        #change the balance
        oldBalance = self._balance
        self._balance -= amount
        
        #provide the new balance to the caller to avoid a getBalance() call
        return self._balance






