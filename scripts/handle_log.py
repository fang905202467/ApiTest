# -*- coding: UTF-8 -*-
# @Time : 2020/5/7 17:44 
# @Author : fangkun
# @File : handle_log.py 
# @Software: PyCharm

import logging
from scripts.handle_config import do_config


class Handlelog:

    def __init__(self):
        # 1.定义日志收集器
        self.case_logger = logging.getLogger(do_config.get_config("log", "logging_name"))  # 创建一个logger对象

        # 2.指定日志收集器的日志等级
        # NOTSET(0), DEBUG(10), INFO(20), WARNING(30), ERROR(40), CRITICAL(50)
        self.case_logger.setLevel(do_config.get_config("log", "logging_level"))  # 只能手机当前等级和当前等级以上的级别日志
        # self.case_logger.setLevel("DEBUG")

        # 3.定义日志输出渠道
        # 输出到控制台
        console_handle = logging.StreamHandler()  # handler对象
        # 输出到文件
        file_handle = logging.FileHandler(do_config.get_config("log", "file_name"), encoding="utf-8")

        # 4.指定日志输出渠道的日志等级
        console_handle.setLevel(do_config.get_config("log", "console_level"))
        file_handle.setLevel(do_config.get_config("log", "file_level"))

        # 5.定义日志显示格式
        simple_formatter = logging.Formatter(do_config.get_config("log", "simple_formatter"))
        verbose_formatter = logging.Formatter(do_config.get_config("log", "verbose_formatter"))

        console_handle.setFormatter(simple_formatter)  # 控制台使用定义的日志格式
        file_handle.setFormatter(verbose_formatter)  # 文件使用定义的日志格式

        # 6.将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        '''
        获取logger日志器对象
        :return:
        '''
        return self.case_logger


# do_log = Handlelog()
# case_logger = do_log.get_logger()
do_log = Handlelog().get_logger()

if __name__ == '__main__':
    case_logger = Handlelog().get_logger()
    case_logger.debug("这是一个debug级别日志")  # 手动记录日志
    case_logger.info("这是一个info级别日志")
    case_logger.warning("这是一个warning级别日志")
    case_logger.error("这是一个error级别日志")
    case_logger.critical("这是一个critical级别日志")
