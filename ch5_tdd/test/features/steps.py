from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp
from ch5_tdd import Account
from ch5_tdd import app, BANK


@step("I create the following account:")
def i_create_the_following_account(step):
    for row in step.hashes:
        account = Account(row['account_number'], row['balance'])
        BANK.add_account(account)


@step(u'I visit the homepage')
def given_i_visit_the_homepage(step):
    world.browser = TestApp(app)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)


@step(u'I enter the account number "([^"]*)"')
def when_i_enter_the_account_number_group1(step, account_number):
    form = world.response.forms['account-form']
    form['account_number'] = account_number
    world.form_response = form.submit()
    assert_equal(world.form_response.status_code, 200)


@step(u'I see a balance of "([^"]*)"')
def then_i_see_a_balance_of_group1(step, expected_balance):
    assert_in("Balance: {}".format(expected_balance), world.form_response.text)