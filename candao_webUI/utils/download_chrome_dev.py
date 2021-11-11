# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: download_chrome_dev.py
  @time: 2021/11/9 22:54
  @desc:
"""
import requests
import zipfile

from config.conf import cm

DRIVERS_PATH = cm.DRIVER_PATH


class Download_dev():

    def download_driver(self, download_url):
        '''下载文件'''
        file = requests.get(download_url)
        with open(DRIVERS_PATH + "\chromedriver.zip", 'wb') as zip_file:  # 保存文件到脚本所在目录
            zip_file.write(file.content)
            print('下载成功')


    def unzip_driver(self,path):
        '''解压Chromedriver压缩包到指定目录'''
        f = zipfile.ZipFile(DRIVERS_PATH + "\chromedriver.zip", 'r')
        for file in f.namelist():
            f.extract(file, path)
