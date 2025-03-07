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
        protected string _acctHolderName;

        /// <summary>
        /// the account number
        /// </summary>
        protected int _acctNo;

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

        public virtual decimal? Deposit(double amount)
        {
            //check if the amount is less than zero
            if (amount < 0)
            {
                //if less than zero, return null
                return null;
            }

            //convert the amount to a decimal
            decimal decimalAmount = (decimal)(double)amount;

            //add the amount to the balance
            _balance += decimalAmount;

            //return the new balance
            return _balance;
        }

        public virtual decimal? Withdraw(double amount)
        {
            //check if the amount is less than zero
            if (amount < 0)
            {
                //if less than zero, return null
                return null;
            }

            //convert the amount to a decimal
            decimal decimalAmount = (decimal)(double)amount;

            //subtract the amount to the balance
            
            _balance -= decimalAmount;

            //return the new balance
            return _balance;
        }

        public override string ToString()
        {
            return $" Account Type: Default, Account Number: {_acctNo}, Holder Name: {_acctHolderName}, Interest rate: {_annualIntrRate}, Balance: {_balance}";
        }

        #endregion
    }
}
