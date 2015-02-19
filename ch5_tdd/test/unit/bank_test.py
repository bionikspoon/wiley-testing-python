import unittest
from ch5_tdd import Account
from ch5_tdd import Bank


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_bank_is_initially_empty(self):
        self.assertEqual({}, self.bank.accounts)
        self.assertEqual(len(self.bank.accounts), 0)

    def test_add_account(self):
        account_1 = Account(001, 50)
        account_2 = Account(002, 100)

        self.bank.add_account(account_1)
        self.bank.add_account(account_2)

        self.assertEqual(len(self.bank.accounts), 2)

    def test_get_account_balance(self):
        account_1 = Account(001, 50)

        self.bank.add_account(account_1)

        self.assertEqual(self.bank.get_account_balance(001), 50)


if __name__ == '__main__':
    unittest.main()
