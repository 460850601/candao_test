# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: Run_Testcase.py
  @time: 2021/11/6 20:39
  @desc:
"""

import sys
import subprocess

# 获取系统属性
SYS_INFO = sys.platform.startswith('win')


def main():
    steps = [
        # 判断sys.platform是否为win开头，如果是执行"venv\\Script\\activate" 否则 "source venv/bin/activate"
        "venv\\Script\\activate" if SYS_INFO else "source venv/bin/activate",
        # 清理旧报告
        "pytest --alluredir allure-results --clean-alluredir",
        #  生成报告
        "allure generate allure-results -c -o allure-report",
        # 打开报告
        "allure open allure-report"
    ]
    for step in steps:
        subprocess.run("call " + step if SYS_INFO else step, shell=True)


if __name__ == "__main__":
    main()
