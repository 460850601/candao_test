# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: test_001_main.py
  @time: 2021/11/6 9:48
  @desc:
"""

import allure
import pytest

from common.readconfig import ini
from page_object.login import LoginPage


@allure.story("测试主流程：顺利通过的全套流程")
class TestOverview:

    @allure.step("登录")
    @pytest.fixture(scope="function")
    def login(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
        login.input_user('admin')
        login.input_pwd('Qwase899130@@')
        login.btn_login()

    @allure.step("登录后的操作")
    @pytest.mark.usefixtures("login")
    def test_001(self, drivers):
        """登录后操作"""
        print("登录后操作")

# pytest会自动搜索测试用例，不用在这里调用，这里只是为了单个文件调试的时候使用
# if __name__  == '__main__' :
#     pytest.main(['test_001_main.py','-s'])#'--capture=no'
