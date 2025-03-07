using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

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

        public Account OpenAccount(int accountNumber, string accountHolderName)
        {
            //Create the new account
            Account newAccount = new Account(accountNumber, accountHolderName);

            //Return the new account
            return newAccount;
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


        #endregion
    }
}
