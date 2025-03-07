namespace BankApp;

public partial class MainPage : ContentPage
{
	private Bank _bank;

	public MainPage(Bank bank)
	{
		_bank = bank;

		InitializeComponent();

        _lstBankAccounts.ItemsSource = _bank.Accounts;
    }

    private void OnCreateAccount(object sender, EventArgs e)
    {
        //Read the accounts properties
        //string accountType = _pckAccountType.SelectedItem as string;
        int accountNumber = int.Parse(_txtAcctNo.Text);
        string accountHolderName = _txtAcctHolderName.Text;

        //realAccountType = this.DetermineType(accountType);

        //Create an Account object based on the provided information
        Account createdAccount = _bank.OpenAccount(accountNumber, accountHolderName);

        //Add the account to the Bank list
        _bank.Accounts.Add(createdAccount);

    }
}
