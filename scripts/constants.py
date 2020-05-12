# -*- coding: utf-8 -*-
# @Time : 2020/5/12 17:26
# @Author : fangkun
# @File : constants.py
# @Software: PyCharm

import os
#动态获取config（配置文件）的绝对路径
# one_path = os.path.abspath(__file__) #获取当前py文件绝对路径
#one_path = os.path.dirname(__file__) #获取当前路径上一级目录所在位置的绝对路径
# two_path = os.path.dirname(one_path)  #获取当前路径上一级目录所在位置的绝对路径
# three_path = os.path.dirname(two_path)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIGS_DIR = os.path.join(BASE_DIR,"configs")
CONFIGS_FILE_PATH = os.path.join(CONFIGS_DIR,"config.conf")

#动态获取excel的绝对路径
DATAS_DIR = os.path.join(BASE_DIR,"datas")
DATAS_FILE_PATH = os.path.join(DATAS_DIR,"cases.xlsx")
#动态获取log文件的绝对路径
LOGS_DIR = os.path.join(BASE_DIR,"logs")
#动态获取报告文件的绝对路径
REPORTS_DIR = os.path.join(BASE_DIR,"reports")

