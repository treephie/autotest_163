import unittest

# suite = unittest.defaultTestLoader.discover('../test_case/', pattern='test*.py')
suite = unittest.defaultTestLoader.discover('../test_case/', pattern='test_send*.py')

runner = unittest.TextTestRunner()
runner.run(suite)