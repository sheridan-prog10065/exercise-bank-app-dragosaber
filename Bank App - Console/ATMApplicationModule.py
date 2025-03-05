from BankModule import Bank
from AccountModule import Account
from ATMModule import Atm

class ATMApplication:
    def run(self):
        #use exception handling to ensure the application does not crash
        try:
            #create a bank for a more real-life like implementation
            bank = Bank()
            bank.loadAccountData()

            #create ATM nad link it with the bank
            atm = Atm(bank)

            #start the ATM machine
            atm.start()

        except Exception as e:
            print('An error occurred with the following message: ', e)


