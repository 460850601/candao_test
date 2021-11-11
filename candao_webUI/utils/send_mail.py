# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: send_mail.py
  @time: 2021/11/7 14:50
  @desc:
"""

import zmail
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from config.conf import cm


def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': 'xxxxxxxxxx@qq.com',
            'subject': '测试报告',
            'content_html': content_html,
            'attachments': [cm.REPORT_FILE, ]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))


if __name__ == "__main__":
    '''请先在config/conf.py文件设置QQ邮箱的账号和密码'''
    send_report()
