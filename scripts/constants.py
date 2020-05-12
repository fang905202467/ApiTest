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

#

pass