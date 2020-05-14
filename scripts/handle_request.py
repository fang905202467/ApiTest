# -*- coding: UTF-8 -*-
# @Time : 2020/5/9 16:48 
# @Author : fangkun
# @File : handle_request.py 
# @Software: PyCharm

import requests
import json

class HandleRequest:
    '''
    处理请求
    '''
    def __init__(self):
        self.one_session = requests.Session()  #创建session会话对象

    def to_request(self, url, data, method='post', is_json=False):
        '''

        :param url: 测试接口
        :param method: 请求方式
        :param data: 参数
        :param is_json: 标记，用来判断传参格式
        :return:
        '''
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as e:
                data = eval(data)

        method = method.lower()
        if method == 'get':
            res = self.one_session.get(url=url,params=data)
        elif method == 'post':
            if is_json: #这里判断is_json是否为True，如果为true，那么以json格式来传参
                res = self.one_session.post(url=url,json=data)
            else: #如果json为False，那么以www-from的形式来传参
                res = self.one_session.post(url=url,data=data)
        else:
            res = None
            print("不支持【{}】其他方法的请求".format(method))

    def close(self):
        self.one_session.close()

if __name__ == '__main__':
    # do_request = HandleRequest()
    one_session = requests.Session()
    data = '{"eid":"1588222319","name":"小米8798797978发布会","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    data_dict =json.loads(data)
    url = 'http://47.104.90.247:8000/api/add_event/'
    res = one_session.post(url=url, data=data_dict)
    # res = do_request.to_request(url, data, 'post')
    print(res)
