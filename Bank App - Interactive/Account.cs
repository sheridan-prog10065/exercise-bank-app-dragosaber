using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{
    public class Account
    {
        #region Fields
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
        protected double _annualIntrRate;

        /// <summary>
        /// the account balance that gets affected by withdrawls and deposits
        /// </summary>
        protected decimal _balance;

        #endregion

        #region Constructors
        public Account(int acctNo, string acctHolderName)
        {

            _acctNo = acctNo;
            _acctHolderName = acctHolderName;
            _annualIntrRate = 0.0;
            _balance = 0;
        }

        #endregion

        #region Properties
        public string acctHolderName
        {
            get { return _acctHolderName; }
        }

        public int acctNo
        {
            get { return _acctNo; }
        }

        public virtual double annualIntrRate
        {
            get { return _annualIntrRate; }
            set { _annualIntrRate = value; }
        }

        public decimal balance
        {
            get { return _balance; }
        }

        #endregion

        #region Methods
        public override string ToString()
        {
            return $" Account Number: {_acctNo}, Holder Name: {_acctHolderName}, Interest rate: {_annualIntrRate}, Balance: {_balance}";
        }

        #endregion
    }
}
