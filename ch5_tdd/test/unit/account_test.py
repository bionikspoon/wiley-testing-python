import unittest
from ch5_tdd.bank.account import Account


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("001", 50)

    def test_account_object_can_be_created(self):
        self.assertIsInstance(self.account, Account)

    def test_account_object_returns_current_balance(self):
        self.assertEqual(self.account.account_number, "001")
        self.assertEqual(self.account.balance, 50)


if __name__ == '__main__':
    unittest.main()
