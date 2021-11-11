# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: conf.py
  @time: 2021/11/7 21:34
  @desc:
"""

import os,sys
from selenium.webdriver.common.by import By
from utils.times import dt_strftime


BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]


class ConfigManager(object):
    # 项目目录
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(BASE_DIR, 'page_element')

    # 报告目录
    REPORT_FILE = os.path.join(BASE_DIR, 'report.html')
    # 驱动目录
    DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
    # 日志目录
    LOGS_PATH = os.path.join(BASE_PATH, 'logs')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '4xxxx@qq.com',  # 切换成你自己的地址
        'password': 'xxxxx',  #开启smtp服务后的授权码,在qq邮箱-设置-账户中可以开启smtp服务并获取授权码
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        'xxxxx@qq.com',
    ]

    @property  #创建只读属性
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.BASE_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.BASE_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()
# if __name__ == '__main__':
#     print(cm.DRIVER_PATH)
