# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: conftest.py
  @time: 2021/11/7 21:50
  @desc:
"""
from config.conf import cm
import pytest
from py.xml import html
from selenium import webdriver
from utils.check_driver import ck
from common.readconfig import ini
from utils.del_old_log import del_log

CHROMEDRIVER_PATH = cm.DRIVER_PATH + '\chromedriver.exe'
IEDRIVER_PATH = cm.DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJSDRIVER_PATH = cm.DRIVER_PATH + '\phantomjs.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH, 'ie': IEDRIVER_PATH,
                   'phantomjs': PHANTOMJSDRIVER_PATH}
driver = None


class UnSupportBrowserTypeError:
    pass


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    del_log.delete_log()
    global driver
    browser_type = ini.executable
    _type = browser_type.lower()
    if _type in TYPES:
        browser = TYPES[_type]
        if browser == TYPES['chrome']:
            ck.Run_download_driver()
            driver = browser(executable_path=EXECUTABLE_PATH[_type])
            driver.maximize_window()
    else:
        ck.Run_download_driver()
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    extra = getattr(report, 'extra', [])


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))


def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return driver.get_screenshot_as_base64()
