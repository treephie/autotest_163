# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import time


class Mail:
    """
    邮件类，提供发送邮件的方法
    """

    def __init__(self, mail_from, mail_to, mail_subject, mail_attach):
        self.mail_from = mail_from
        self.mail_to = mail_to
        self.mail_subject = mail_subject
        self.mail_attach = mail_attach
        f = open(mail_attach, 'rb')
        self.mail_body = f.read()
        f.close()

    def send_mail(self):

        msg = MIMEText(self.mail_body, 'html', 'utf-8')
        msg['from'] = self.mail_from
        msg['to'] = self.mail_to
        msg['Subject'] = self.mail_subject
        msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        smtp = smtplib.SMTP()
        smtp.connect('smtp.163.com')
        smtp.login('phlearningtest@163.com', 'phtest001')
        # print self.mail_from, self.mail_to, msg.as_string()
        smtp.sendmail(self.mail_from, self.mail_to, msg.as_string())
        smtp.quit()
        print 'email has send out !'


if __name__ == '__main__':
    Mail('phlearningtest@163.com', '838927564@qq.com', u'163邮箱测试报告', u'F:/学习/web自动化：Python+Selenium/实战-163邮箱/autotest_163/report/report1499138546.63.html').send_mail()
