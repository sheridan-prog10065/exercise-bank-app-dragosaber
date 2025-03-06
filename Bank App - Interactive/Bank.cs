using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{

    public class Bank
    {
        /// <summary>
        /// the list of accounts managed by the bank
        /// </summary>
        private List<Account> _accountList;

        public Bank()
        {
            _accountList = new List<Account>();
        }
    }
}
