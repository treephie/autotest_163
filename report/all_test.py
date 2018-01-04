# coding: utf-8
import unittest
import HTMLTestRunner
import time, os
from mail import Mail


def get_report(file_dir):
    """
    在报告目录下获取最新生成的测试报告并发挥
    :param file_dir: 测试报告的路径
    :return: 最新的报告文件名
    """
    lists = os.listdir(file_dir)
    lists.sort()
    return os.path.join(file_dir, lists[-1])


test_case_dir = '../test_case/'
report_filename = './report' + str(time.time()) + '.html'

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
    fp = file(report_filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'163邮箱测试报告',
                                           description=u'用例执行情况')
    runner.run(suite)
    fp.close()

    report = get_report('./')
    Mail.Mail('phlearningtest@163.com', '838927564@qq.com', u'163邮箱测试报告', report).send_mail()
