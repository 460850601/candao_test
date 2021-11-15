# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: del_old_log.py
  @time: 2021/11/14 21:27
  @desc:
"""
import os
from utils.loggers import log
from config.conf import cm
from common.readconfig import ini


log = log
cm = cm


class DelOldLog():
    logs_path = cm.LOGS_PATH
    max_file = ini.max_log_file
    def __get_file_list(self):
        self.dir_list = os.listdir(self.logs_path)
        if not self.dir_list:
            log.info('不存在日志文档')
            return
        else:
            # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            self.dir_list = sorted(self.dir_list, key=lambda x: os.path.getmtime(os.path.join(self.logs_path, x)))
            # print(dir_list)
            return self.dir_list

    def delete_log(self):

        dir_list = self.__get_file_list()
        if len(dir_list) > self.max_file:
            for i in range(len(dir_list)):
                if len(self.__get_file_list()) > self.max_file:
                    os.remove(self.logs_path + '\\' + dir_list[i])


del_log = DelOldLog()

if __name__ == "__main__":
    del_log.delete_log()