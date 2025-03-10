﻿using Microsoft.Maui;

namespace BankApp;

public partial class MainPage : ContentPage
{
	private Bank _bank;

    private int _depositClickCount;
    private int _withdrawClickCount;

    public MainPage(Bank bank)
	{
		_bank = bank;

		InitializeComponent();

        _lstBankAccounts.ItemsSource = _bank.Accounts;
    }

    private void OnCreateAccount(object sender, EventArgs e)
    {
        //Read the accounts properties
        string accountType = _pckAccountType.SelectedItem as string;
        int accountNumber = int.Parse(_txtAcctNo.Text);
        string accountHolderName = _txtAcctHolderName.Text;

        //Create an Account object based on the provided information
        Account createdAccount = _bank.OpenAccount(accountNumber, accountHolderName, accountType);

        //Add the account to the Bank list
        _bank.Accounts.Add(createdAccount);
    }

    private async void OnDeposit(object sender, EventArgs e)
    {
        _depositClickCount++;

        if (_depositClickCount == 1)
        {
            _txtDepositAmount.IsVisible = true;
            _txtWithdrawAmount.IsVisible = false;
            _withdrawClickCount = 0;
            _txtDepositAmount.Text = "";
        }
        else if (_depositClickCount == 2)
        {
            if (_txtDepositAmount.Text == "")
            {
                _txtDepositAmount.Text = "Please enter an amount to deposit";

                await Task.Delay(2000);

                _depositClickCount = 0;
            }
            else
            {
                int depositedAmount = int.Parse(_txtDepositAmount.Text);

                Account selecteddAccount = (Account)_lstBankAccounts.SelectedItem;

                decimal? attemptDeposit = selecteddAccount.Deposit(depositedAmount);

                _lstBankAccounts.ItemsSource = null;
                _lstBankAccounts.ItemsSource = _bank.Accounts;

                if (attemptDeposit == null)
                {
                    _txtDepositAmount.Text = $"You deposited ${depositedAmount}";
                }
                else
                {
                    _txtDepositAmount.Text = $"You deposited ${attemptDeposit}";
                }

                await Task.Delay(4000);

                _depositClickCount = 0;
                _withdrawClickCount = 0;
                _txtDepositAmount.Text = "";
                _txtDepositAmount.IsVisible = false;
            }
        }
    }

    private async void OnWithdraw(object sender, EventArgs e)
    {
        _withdrawClickCount++;

        if (_withdrawClickCount == 1)
        {
            _txtDepositAmount.IsVisible = false;
            _txtWithdrawAmount.IsVisible = true;
            _depositClickCount = 0;
            _txtWithdrawAmount.Text = "";
        }
        else if (_withdrawClickCount == 2)
        {
            if (_txtWithdrawAmount.Text == "")
            {
                _txtWithdrawAmount.Text = "Please enter an amount to withdraw";

                await Task.Delay(2000);

                _withdrawClickCount = 0;
            }
            else
            {
                int withdrawAmount = int.Parse(_txtWithdrawAmount.Text);

                Account selectedAccount = null;

                if (_lstBankAccounts.SelectedItem is SavingsAccount savingsAccount)
                {
                    selectedAccount = savingsAccount;
                }
                else if (_lstBankAccounts.SelectedItem is ChequingAccount chequingAccount)
                {
                    selectedAccount = chequingAccount;
                }
                else if (_lstBankAccounts.SelectedItem is Account account)
                {
                    selectedAccount = account;
                }

                decimal? attemptWithdraw = null;

                if (selectedAccount != null)
                {
                    attemptWithdraw = selectedAccount.Withdraw(withdrawAmount);
                }

                Console.WriteLine(attemptWithdraw);

                _lstBankAccounts.ItemsSource = null;
                _lstBankAccounts.ItemsSource = _bank.Accounts;

                if (attemptWithdraw != null)
                {
                    _txtWithdrawAmount.Text = $"You withdrew ${withdrawAmount}";
                }
                else
                {
                    _txtWithdrawAmount.Text = "ERROR";
                }

                await Task.Delay(4000);

                _withdrawClickCount = 0;
                _depositClickCount = 0;
                _txtWithdrawAmount.Text = "";
                _txtWithdrawAmount.IsVisible = false;
            }
        }
    }
}
