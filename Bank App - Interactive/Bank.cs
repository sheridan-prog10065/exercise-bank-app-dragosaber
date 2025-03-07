using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.VisualBasic;

namespace BankApp
{

    public class Bank
    {

        #region Fields
        /// <summary>
        /// The list of accounts managed by the bank
        /// </summary>
        private ObservableCollection<Account> _accountList;

        #endregion

        #region Constructors
        public Bank()
        {
            _accountList = new ObservableCollection<Account>();

            CreateDefaultBooks();
        }

        #endregion

        #region Properties

        public ObservableCollection<Account> Accounts
        {
            get
            {
                return _accountList;
            }
        }

        #endregion

        #region Methods

        public Account OpenAccount(int accountNumber, string accountHolderName, string accountType)
        {
            switch (accountType)
            {
                case "Savings":
                    //Create the new Savings account
                    SavingsAccount newSavingsAccount = new SavingsAccount(accountNumber, accountHolderName);

                    //Return the new Savings account
                    return newSavingsAccount;

                case "Chequing":
                    //Create the new Chequing account
                    ChequingAccount newChequingAccount = new ChequingAccount(accountNumber, accountHolderName);

                    //Return the new Chequing account
                    return newChequingAccount;

                default:
                    //Create the new account
                    Account newAccount = new Account(accountNumber, accountHolderName);

                    //Return the new account
                    return newAccount;
            }
        }

        public Account? FindAccount(int acctNo)
        {
            //search through the bank list until one is found with the given acctNo
            foreach (Account account in _accountList)
            {
                //return the account to the user
                if (account.acctNo == acctNo)
                    return account;
            }
            //if no account is found, return none
            return null;
        }

        private void CreateDefaultBooks()
        {
            //create 3 default accounts
            SavingsAccount account1 = new SavingsAccount(40536, "Jolyne Cujoh");
            ChequingAccount account2 = new ChequingAccount(1098272938, "Helly R");
            SavingsAccount account3 = new SavingsAccount(7274, "Jack Cooper");

            //add money to the accounts
            account1.Deposit(10000);
            account1.Deposit(6);
            account1.Deposit(1041);

            //add the accounts to the bank
            _accountList.Add(account1);
            _accountList.Add(account2);
            _accountList.Add(account3);
        }

        #endregion
    }
}
