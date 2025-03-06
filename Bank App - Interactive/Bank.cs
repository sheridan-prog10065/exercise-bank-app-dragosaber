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
    }
}
