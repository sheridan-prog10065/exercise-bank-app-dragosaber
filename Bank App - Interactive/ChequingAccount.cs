using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{
    public class ChequingAccount : Account
    {
        #region Fields
        /// <summary>
        /// The overdraft limit for chequing accounts
        /// </summary>
        private const int OVERDRAFT_LIMIT = 500;

        /// <summary>
        /// The maximum interest rate for chequing accounts
        /// </summary>
        private const double MAX_INTEREST_RATE = 1.0;

        #endregion

        #region Constructors
        public ChequingAccount(int acctNo, string acctHolderName) : base(acctNo, acctHolderName)
        {

        }

        #endregion

        #region Properties
        public override double annualIntrRate
        {
            get { return _annualIntrRate; }
            set
            {
                if (value > MAX_INTEREST_RATE)
                {
                    annualIntrRate = MAX_INTEREST_RATE;
                }
                else
                {
                    annualIntrRate = value;
                }
            }
        }

        #endregion

        #region Methods

        public override decimal? Withdraw(double amount)
        {
            //check if the amount is less than zero
            if (amount < 0)
            {
                //if less than zero, return null
                return null;
            }

            //convert the amount to a decimal
            decimal decimalAmount = (decimal)(double)amount;

            //check if the amount is greater than the balance + the overdraft limit
            if (decimalAmount > _balance + OVERDRAFT_LIMIT)
            {
                //if less than zero, return null
                return null;
            }

            //add the amount to the balance
            _balance -= decimalAmount;

            //return the new balance
            return _balance;
        }

        public override string ToString()
        {
            return $" Account Type: Chequing, Number: {_acctNo}, Holder Name: {_acctHolderName}, Interest rate: {_annualIntrRate}, Balance: {_balance}, Max Overdraft: $500";
        }

        #endregion
    }
}
