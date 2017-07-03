# coding: utf-8
"""
测试登录的各种异常情况
"""
import unittest
from selenium import webdriver
from test_case.public import login
from time import sleep
import xml.dom.minidom


# 读取测试文件
dom = xml.dom.minidom.parse('../test_data/login_data.xml')
root = dom.documentElement


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = root.getElementsByTagName('url')[0].firstChild.data

    # 输入用户名和密码为空
    def test_null(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 尝试登录
        login_info = root.getElementsByTagName('null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        login.login(self, username, password)
        text = driver.find_element_by_css_selector('.ferrorhead').text
        self.assertEqual(text, error_msg)

    # 输入用户名、密码为空
    def test_pwd_null(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 尝试登录
        login_info = root.getElementsByTagName('pwd_null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        login.login(self, username, password)
        text = driver.find_element_by_css_selector('.ferrorhead').text
        self.assertEqual(text, error_msg)

    # 输入用户名为空、密码
    def test_user_null(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 尝试登录
        login_info = root.getElementsByTagName('user_null')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        login.login(self, username, password)
        text = driver.find_element_by_css_selector('.ferrorhead').text
        self.assertEqual(text, error_msg)

    # 输入用户名和密码错误
    def test_error(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 尝试登录
        login_info = root.getElementsByTagName('error')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        error_msg = login_info[0].firstChild.data

        login.login(self, username, password)
        text = driver.find_element_by_css_selector('.ferrorhead').text
        self.assertEqual(text, error_msg)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
