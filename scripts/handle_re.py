# -*- coding: UTF-8 -*-
"""
======================
@author:fangkun
@time:2020/5/13:13:42
======================
"""
#正则表达式：是一个查找、搜索、替换文本的一种格式语言
import re

#1.创建原始字符串（待替换的字符串）
src_str = '{"eid":"${not_existed_id}","name":"小米10发布会","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
#2.定义模式字符串去进行匹配
#match方法:是从头开始匹配的
# res = re.match(r'not_existed_id', src_str) #如果匹配不上就返回None
# res = re.match(r'{"eid"', src_str) #如果能匹配上，就返回match对象
# print(res.group()) #使用group获取到匹配内容
#search方法(从头开始找，找到匹配值就结束不找了)，返回字符串
#如果能匹配上，就返回match对象
#匹配不上返回None
# res1 = re.search(r'not_existed_id', src_str)
# res1 = re.search(r'\${not_existed_id}', src_str) #这里$有特殊含义需要\转义
#findall方法（从头开始找，找到所有匹配值，返回一个列表）
# res2 = re.findall(r'i', src_str) #匹配
#获取匹配到的结果
# res1.group()

#替换sub方法
#第一个参数为模式字符串
#第二个参数为新的字符串
#第三个参数为原始字符串
#如果能匹配上，那么返回替换之后的字符串
# res3 = re.sub(r'\${not_existed_id}', '15882223197' ,src_str)
#如果匹配不上，那么直接返回原始字符串
# res3 = re.sub(r'\${not_e123123ed_id}', '15882223197' ,src_str)

# if re.search(r'\${\w+}', src_str):  #\w+ 匹配所有字符串
if re.search(r'\${not_existed_id}', src_str):
    res3 = re.sub(r'\${not_existed_id}', '15882223197' ,src_str)
    print(res3)
else:
    print("无法匹配原始字符串")


