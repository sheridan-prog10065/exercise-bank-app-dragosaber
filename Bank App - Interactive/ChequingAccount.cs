using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BankApp
{
    public class ChequingAccount : Account
    {
        /// <summary>
        /// The overdraft limit for chequing accounts
        /// </summary>
        private const int OVERDRAFT_LIMIT = 500;

        /// <summary>
        /// The maximum interest rate for chequing accounts
        /// </summary>
        private const double MAX_INTEREST_RATE = 1.0;
    }
}
