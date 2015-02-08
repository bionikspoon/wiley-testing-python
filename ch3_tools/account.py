import requests

from ch3_tools.ConnectionError import ConnectionError


class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        try:
            return self.di.get(id_num)
        except ConnectionError:
            result = "Connection error occurred. Try Again."
        return result

    def get_current_balance(self, id_num):
        response = requests.get("http://myapp.dev/%s" % id_num)
        return {'status': response.status_code,
                'data': response.text}