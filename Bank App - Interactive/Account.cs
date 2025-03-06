using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{
    public class Account
    {
        /// <summary>
        /// the name of the account holder
        /// </summary>
        private string _acctHolderName;

        /// <summary>
        /// the account number
        /// </summary>
        private int _acctNo;

        /// <summary>
        /// the annual interest rate applicable on the balance
        /// </summary>
        private double _annualIntrRate;

        /// <summary>
        /// the account balance that gets affected by withdrawls and deposits
        /// </summary>
        private decimal _balance;
    }
}
