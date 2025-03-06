using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{
    public class SavingsAccount : Account
    {
        /// <summary>
        /// The matching deposit ratio. For every dollar deposit this account willautomatically be credited with 0.5 dollars.
        /// </summary>
        private const double MATCHING_DEPOSIT_RATIO = 0.5;

        /// <summary>
        /// The minimmum interest rate for savings accounts
        /// </summary>
        private const double MIN_INTEREST_RATE = 3.0;
    }
}
