# coding: utf-8
"""
测试搜索邮件
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_case.public import login
from time import sleep
import xml.dom.minidom


# 读取测试文件
dom = xml.dom.minidom.parse('../test_data/login_data.xml')
root = dom.documentElement


class TestSearch(unittest.TestCase):
    u"""测试搜索邮件"""
    def setUp(self):
        options = self.driver = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.base_url = root.getElementsByTagName('url')[0].firstChild.data

    # 搜索
    def test_search(self):
        u"""搜索邮件"""
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 输入搜索关键字
        driver.find_element_by_css_selector("input.nui-ipt-input").send_keys('ph')
        driver.find_element_by_css_selector("input.nui-ipt-input").send_keys(Keys.ENTER)

        sleep(3)
        text = driver.find_element_by_class_name("nui-title-text").text
        self.assertIn(u'搜索结果', text)
        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
