# coding: utf-8


# 登录
def login(self, username, password):
    driver = self.driver
    driver.switch_to.frame("x-URS-iframe")
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("dologin").click()


# 登出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text(u'退出').click()