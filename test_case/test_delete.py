# coding: utf-8
"""
测试删除邮件
"""
import unittest
from selenium import webdriver
from test_case.public import login
from time import sleep
import xml.dom.minidom


# 读取测试文件
dom = xml.dom.minidom.parse('../test_data/login_data.xml')
root = dom.documentElement


class TestDelete(unittest.TestCase):
    u"""测试删除邮件"""
    def setUp(self):
        options = self.driver = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.base_url = root.getElementsByTagName('url')[0].firstChild.data

    # 删除
    def test_delete(self):
        u"""删除邮件"""
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 勾选
        driver.find_element_by_xpath("//span[@class='nui-tree-item-text' and @title='已发送']").click()
        driver.find_element_by_css_selector("span.nui-chk-symbol").click()
        spans = driver.find_elements_by_css_selector(".nui-btn-text")
        for s in spans:
            if s.text == u'删 除':
                s.click()

        text = driver.find_element_by_css_selector("span.nui-tips-text>a").text
        self.assertIn(u'已删除', text)
        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
