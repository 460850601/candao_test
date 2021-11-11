# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: loggers.py
  @time: 2021/11/9 21:51
  @desc:
"""
import os, time
import os.path

import logging
import logging.handlers
from config.conf import cm

LOGS_PATH = cm.LOGS_PATH


class Logging(object):

    def __init__(self):
        # 不存在logs文件则新建
        if not os.path.exists(LOGS_PATH):
            os.mkdir(LOGS_PATH)
        log_file = os.path.join(LOGS_PATH, "{}.log".format(time.strftime("%Y%m%d")))

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        self.logging_msg_format = '[%(asctime)s] [%(levelname)s] [%(module)s.py-line:%(lineno)d] %(message)s'
        self.formater = logging.Formatter(self.logging_msg_format)

        self.fileHandler = logging.FileHandler(log_file, mode='a', encoding="UTF-8")
        self.fileHandler.setFormatter(self.formater)
        self.fileHandler.setLevel(logging.INFO)

        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.console.setFormatter(self.formater)

        self.logger.addHandler(self.fileHandler)
        self.logger.addHandler(self.console)

    # def getloger(self):
    #     return self.logger


log = Logging().logger
