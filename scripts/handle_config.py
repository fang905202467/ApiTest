# -*- coding: UTF-8 -*-
# @Time : 2020/5/6 17:47 
# @Author : 隔壁老方
# @File : handle_config.py 
# @Software: PyCharm

from configparser import ConfigParser


class HandleConfig:

    def __init__(self, filename):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def get_config(self, area, option):
        value = self.config.get(area, option)
        return value

    def get_config_int(self, area, option):
        value = self.config.getint(area, option)
        return value

    def get_config_float(self, area, option):
        value = self.config.getfloat(area, option)
        return value

    def get_config_bool(self, area, option):
        value = self.config.getboolean(area, option)
        return value

    def get_config_eval(self, area, option):
        value = eval(self.config.get(area, option))
        return value

    @staticmethod
    def write_config(datas, filename):
        msg = "传入数据错误,应为嵌套字典的字典"
        if isinstance(datas, dict):
            for value in datas.values():
                if not isinstance(value, dict):
                    return msg
                else:
                    config = ConfigParser()
                    for key in datas:  # 用for循环 把datas中的key值赋值给key，
                        config[key] = datas[key]  # datas[key]是datas中的字典数据 赋值给config[key]
                    with open(filename, "w") as file:
                        config.write(file)
        else:
            return msg


do_config = HandleConfig("config.conf")

if __name__ == '__main__':
    # do_config = HandleConfig("config.conf")
    # value = do_config.get_config("file path","cases_path")
    # print(value)
    data = {
        "handle": {
            "1": "wode "
        }
    }
    do_config = HandleConfig("write_config.ini")
    do_config.write_config(datas=data, filename="write_config.ini")
