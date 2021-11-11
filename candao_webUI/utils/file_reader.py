# -*- encoding: utf-8 -*-

"""
  @author: liuzhihua
  @contact: gotoyiyi@gmail.com
  @software: testclass
  @file: file_reader.py
  @time: 2021/11/8 22:40
  @desc:
"""

import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None


    @property  #私有方法装饰器
    def data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


# xlrd版本要使用1.20,太高版本打开xlsx格式报错
class ReaderExcel:
    def __init__(self,excel,sheet=0,title_lind=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在')
        self.sheet = sheet
        self.title_lind = title_lind
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int,str]:
                raise SheetTypeError('请输入整数或有效的sheet名')
            elif type(self.sheet) == int:
                sh = workbook.sheet_by_index(self.sheet)
            else:
                sh = workbook.sheet_by_name(self.sheet)

            if self.title_lind:
                title =sh.row_values(0)
                for col in range(1,sh.nrows):
                    self._data.append(dict(zip(title,sh.row_values(col))))
            else:
                for col in range(0,sh.nrows):
                    self._data.append(sh.row_values(col))
        return self._data





if __name__ == '__main__':

    e = 'D:/homework/webUI_testDemo/data/user.xls'
    reader = ReaderExcel(e, title_lind=True)
    print(reader.data)



