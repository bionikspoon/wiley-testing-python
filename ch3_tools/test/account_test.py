import unittest

from mock import Mock, patch

from ch3_tools.ConnectionError import ConnectionError

from ch3_tools.Account import Account


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_data_interface = Mock()
        self.account = Account(self.mock_data_interface)

    def test_account_returns_data_for_id(self):
        account_data = {"id": "1", "name": "test"}
        self.mock_data_interface.get.return_value = account_data
        self.assertDictEqual(account_data, self.account.get_account(1))

    def test_account_when_connect_exception_raised(self):
        self.mock_data_interface.get.side_effect = ConnectionError()
        self.assertEqual("Connection error occurred. Try Again.",
                         self.account.get_account(1))

    @patch('ch3_tools.Account.requests')
    def test_get_current_balance_returns_data_correctly(self, mock_requests):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = 'Some text data'
        mock_requests.get.return_value = mock_response
        self.assertEqual({'status': 200, 'data': 'Some text data'},
                         self.account.get_current_balance('1'))


if __name__ == '__main__':
    unittest.main()
