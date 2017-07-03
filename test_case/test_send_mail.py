# coding: utf-8
"""
测试发送邮件
"""
import unittest
from selenium import webdriver
from test_case.public import login
from time import sleep
import xml.dom.minidom


# 读取测试文件
dom = xml.dom.minidom.parse('../test_data/login_data.xml')
root = dom.documentElement


class TestSendMail(unittest.TestCase):
    def setUp(self):
        options = self.driver = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(10)
        self.base_url = root.getElementsByTagName('url')[0].firstChild.data

    # 只输入收信人发送
    def test_send1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 写信
        driver.find_element_by_xpath("//div[@id='dvNavTop']/ul/li[2]").click()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys('838927564@qq.com')
        driver.find_element_by_xpath("//header[@class='frame-main-cont-head']//span[@class='nui-btn-text']").click()
        driver.find_element_by_css_selector(".nui-msgbox-ft-btns>div>span").click()
        sleep(3)
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn(u'发送成功', text)
        # 退出
        login.logout(self)

    # 输入收信人、主题、正文、附件发送
    def test_send2(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(3)
        # 登录
        login_info = root.getElementsByTagName('normal')
        username = login_info[0].getAttribute('username')
        password = login_info[0].getAttribute('password')
        login.login(self, username, password)
        # 写信
        driver.find_element_by_xpath("//div[@id='dvNavTop']/ul/li[2]").click()
        driver.find_element_by_css_selector("input.nui-editableAddr-ipt").send_keys('838927564@qq.com')
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @maxlength='256']").send_keys(u'自动发送的主题')

        frame = driver.find_element_by_css_selector("iframe.APP-editor-iframe")
        driver.switch_to.frame(frame)
        driver.find_element_by_xpath("//body[@class='nui-scroll']").send_keys(u'自动发送的正文内容，啊哈哈哈哈哈')
        driver.switch_to.default_content()

        driver.find_element_by_xpath("//input[@type='file']").send_keys("F:\\attach.txt")
        driver.find_element_by_xpath("//header[@class='frame-main-cont-head']//span[@class='nui-btn-text']").click()
        sleep(3)
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn(u'发送成功', text)
        # 退出
        login.logout(self)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
