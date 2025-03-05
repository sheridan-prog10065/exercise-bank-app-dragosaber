from AccountModule import Account, InvalidValue

class SavingsAccount(Account):
    """Represents a savings account. A saving account has specific business logic. It has
    a minimum interest rate and an additional deposit business rule
    """

    """The matching deposit ratio. For every dollar deposit this account will
    automatically be credited with 0.5 dollars. Defined as a class variable and accessible
    through the name of the class along with the DOT notation"""
    MATCHING_DEPOSIT_RATIO = 0.5

    """The minimmum interest rate for savings accounts. Defined as a class variable and accessible
    through the name of the class along with the DOT notation """
    MIN_INTEREST_RATE = 3.0

    def __init__(self, acctNo=-1, acctHolderName=''):
        """Provide a constructor and ensure the base contstructor gets called

        NOTE: the constructor assigns default values to each parameter allowing the code
        not to supply them (i.e. acct = SavingsAccount()). If the calling code does not supply
        values for the two parameters they will receive these default values. This is used
        when the accounts are created from data files 

        Arguments:
            acctNo          : int   -- the account number, required parameter
            acctHolderName  : str   -- the name of the account holder, required parameter
        """
        Account.__init__(self, acctNo, acctHolderName)
    
    def setAnnualIntrRate(self, newAnnualIntrRatePercentage):
        """
        Change the annual interest rate on the account. Verify the annual interest rate is valid for a savings account

        Arguments:
            newAnnualIntrRatePercentage: float -- the annual interest as a percentage (e.g. 3%)
        """
        #check to ensure the annual interest rate is valid for a checquing account
        if newAnnualIntrRatePercentage < SavingsAccount.MIN_INTEREST_RATE:
            raise InvalidValue('A savings account cannot have an interest rate less than {0}'.format(SavingsAccount.MIN_INTEREST_RATE))
        
        #use the base class to set the annual interest rate
        Account.setAnnualIntrRate(self, newAnnualIntrRatePercentage)

    def deposit(self, amount):
        """Deposit the given amount in the account and return the new balance. For every dollar deposited the
        account will be credited with 0.5 dollars with an automatic deposit
        Arguments:
            amount - the amount to be deposited
        Returns:
            the new account balance AFTER the amount was deposited to avoid a call to getBalance() if needed
        """
        Account.deposit(self, amount + amount * SavingsAccount.MATCHING_DEPOSIT_RATIO)