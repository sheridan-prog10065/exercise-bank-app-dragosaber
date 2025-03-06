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
    }
}
