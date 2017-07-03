import unittest


test_case_dir = '../test_case/'

test_login_list = unittest.defaultTestLoader.discover(test_case_dir, pattern='test_login*.py')
test_send_list = unittest.defaultTestLoader.discover(test_case_dir, pattern='test_send*.py')
test_search_list = unittest.defaultTestLoader.discover(test_case_dir, pattern='test_search*.py')
test_delete_list = unittest.defaultTestLoader.discover(test_case_dir, pattern='test_delete*.py')

suite = unittest.TestSuite()
suite.addTests(test_login_list)
suite.addTests(test_send_list)
suite.addTests(test_search_list)
suite.addTests(test_delete_list)


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)