# coding=utf-8
import smtplib
from email.mime.text import MIMEText
import os, time


# =============定义发送邮件==========
def send_mail(file_new):
    # 发信邮箱
    mail_from='phlearningtest@163.com'
    # 收信邮箱
    mail_to='838927564@qq.com'
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['from'] = mail_from
    msg['to'] = mail_to
    msg['Subject'] = u"自动化测试报告"
    # 定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器，此处用的 163 的 SMTP 服务器
    smtp.connect('smtp.163.com')
    # 用户名密码
    smtp.login('phlearningtest@163.com', 'phtest001')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out !'


# ======查找测试报告目录，找到最新生成的测试报告文件====《Selenium2 Python 自动化测试实战》
def send_report(test_report):
    result_dir = test_report
    lists = os.listdir(result_dir)
    lists.sort()
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    print file_new
    # 调用发邮件模块
    send_mail(file_new)


if __name__ == '__main__':
    send_report(u'F:/学习/web自动化：Python+Selenium/实战-163邮箱/autotest_163/report')
