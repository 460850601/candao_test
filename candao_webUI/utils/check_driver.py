# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: check_driver.py
  @time: 2021/11/9 22:55
  @desc:
"""
import requests
import re
import os
from config.conf import cm
from utils.download_chrome_dev import Download_dev

DRIVERS_PATH = cm.DRIVER_PATH

class Check_Driver(Download_dev):

    def query_driver_version(self,url):
        '''查询最新的Chromedriver版本'''
        rep = requests.get(url).text
        time_list = []  # 用来存放版本时间
        time_version_dict = {}  # 用来存放版本与时间对应关系
        result = re.compile(r'\d.*?/</a>.*?Z').findall(rep)  # 匹配文件夹（版本号）和时间
        for i in result:
            time = i[-24:-1]  # 提取时间
            version = re.compile(r'.*?/').findall(i)[0]  # 提取版本号
            time_version_dict[time] = version  # 构建时间和版本号的对应关系，形成字典
            time_list.append(time)  # 形成时间列表
        latest_version = time_version_dict[max(time_list)][:-1]  # 用最大（新）时间去字典中获取最新的版本号
        return latest_version


    def query_system_driver_version(self):
        '''查询系统内的Chromedriver版本'''
        system_version = os.popen(DRIVERS_PATH + '\chromedriver --version').read()
        return system_version.split(' ')[1]

    def get_path(self):
        '''查询系统内Chromedriver的存放路径,由于mac不能使用指定bash，只能写死路径，有好的解决方案请赐教'''
        system_path = DRIVERS_PATH
        return system_path


    @staticmethod
    def Run_download_driver():
        url = 'http://npm.taobao.org/mirrors/chromedriver/'
        dev = Check_Driver()
        latest_version = dev.query_driver_version(url)
        print('最新的chromedriver版本为：', latest_version)
        version = dev.query_system_driver_version()
        print('当前系统内的Chromedriver版本为：', version)
        if version == latest_version:
            print('当前系统内的Chromedriver已经是最新的')
        else:
            print('当前系统内的Chromedriver不是最新的，需要进行更新')
            download_url = url + latest_version + '/chromedriver_win32.zip'  # 拼接下载链接，更换下载对应系统的driver名称即可
            dev.download_driver(download_url)
            path = dev.get_path()
            print('替换路径为：', path)
            dev.unzip_driver(path)
            # os.unlink()
            print('更新后的Chromedriver版本为：', dev.query_system_driver_version())


ck = Check_Driver()

if __name__ == '__main__':
    ck.Run_download_driver()