# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: login.py
  @time: 2021/11/7 19:38
  @desc:
"""

import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from page.webpage import WebPage
from common.readelement import Element

login = Element('login')  # 获取login.yaml


class LoginPage(WebPage):
    '''登录'''

    def input_user(self, content):
        self.input_text(login['账号'], content)

    def input_pwd(self, content):
        self.input_text(login['密码'], content)

    def btn_login(self):
        self.click(login['登录'])
