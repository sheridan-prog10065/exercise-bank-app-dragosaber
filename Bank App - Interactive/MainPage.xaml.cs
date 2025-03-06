namespace BankApp;

public partial class MainPage : ContentPage
{
	private Bank _bank;

	public MainPage(Bank bank)
	{
		_bank = bank;

		InitializeComponent();

		//_lstBankAccounts.ItemsSource = _bank.Accounts;
    }

    private void OnCreateAccount(object sender, EventArgs e)
    {
    }
}
