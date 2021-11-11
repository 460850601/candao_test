# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: webpage.py
  @time: 2021/11/7 20:24
  @desc:
"""
from selenium import webdriver

from utils.loggers import log

"""
selenium基类
本文件存放了selenium基类的封装方法
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys, os

sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

from config.conf import cm
from utils.times import sleep
from utils import logger


log = log
cm = cm


class WebPage(object):
    """
    selenium基类
    """

    def __init__(self, driver):
        # self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self, url):
        """打开网址并验证"""

        self.driver.set_page_load_timeout(8)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(8)
            logger.info("打开网页：%s" % url)
            log.info("打开禅道主页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(cm.LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def get_attrib(self, locator, value):
        """获取元素属性"""
        logger.info("获取属性")
        ele = self.find_element(locator)
        sleep(0.5)
        return ele.get_attribute(value)


    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def find_element_drag(self, locator):
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        logger.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        sleep(0.5)
        logger.info("输入文本：{}".format(txt))

    def input_enter(self, locator):
        """回车、tab等键入"""

        ele = self.find_element(locator)
        ele.send_keys(Keys.ENTER)

    def click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        logger.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        logger.info("获取文本：{}".format(_text))
        return _text

    def hold_on(self, locator):
        # 定位到要悬停的元素
        move = self.find_element(locator)
        # 对定位到的元素执行悬停操作
        ActionChains(self.driver).move_to_element(move).perform()
        sleep()
        logger.info("悬停元素：{}".format(locator))

    def screen_scoll(self):
        self.driver.execute_script('window.scrollBy(0, 300)')
        sleep(1)

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)
