# -*- coding: UTF-8 -*-
# @Time : 2020/5/12 10:43 
# @Author : fangkun
# @File : handle_mysql.py 
# @Software: PyCharm

import pymysql
import random
from scripts.handle_config import do_config

class HandleMsql:

    def __init__(self):
        self.conn = pymysql.connect(host=do_config.get_config("mysql","host"),
                               user=do_config.get_config("mysql","user"),
                               password=do_config.get_config("mysql","password"),
                               db=do_config.get_config("mysql","db"),
                               port=do_config.get_config_int("mysql","port"),
                               charset=do_config.get_config("mysql","charset"),
                               cursorclass=pymysql.cursors.DictCursor   #这里指定dict游标类获取的数据是字典类型
                               )

        self.cursor = self.conn.cursor()

    # def get_value(self, sql, args=None):
    #     self.cursor.execute(sql, args=args)
    #     self.conn.commit()
    #     return self.cursor.fetchone()
    #
    # def get_values(self, sql, args=None):
    #     self.cursor.execute(sql, args=args)
    #     self.conn.commit()
    #     return self.cursor.fetchall()

    def run(self,sql, args=None, is_more=False):
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def create_id():
        '''
        随机生成一个id
        :return:
        '''
        start_id = ['138','135','199','177']
        start_id = random.choice(start_id)
        end_num = ''.join(random.sample('0123456789', 8))

        return start_id + end_num

    def is_existesd_id(self, id):
        '''
        判断给定的ID在数据库中是否存在
        :param id:11位字符串id
        :return:
        '''
        sql = "SELECT * FROM sign_event WHERE id=%s"
        if self.run(sql, args=(id,)):
            return True
        else:
            return False
    def create_not_existesd_id(self):
        '''
        随机生成一个在数据库中不存在的手机号
        :return:返回一个id字符串
        '''
        while True:
            one_id = self.create_id()
            if not self.is_existesd_id(one_id):
                break

        return one_id

    def obtain_existesd_id(self):
        '''
        获取已存在的id
        :return:
        '''
        id = []
        sql = "SELECT * FROM sign_event"
        result = self.run(sql,is_more=True)
        for i in result:
            id.append(i["id"])

        return id
if __name__ == '__main__':
    # id = 2
    # sql_1 = "SELECT * FROM sign_event WHERE id=%s"
    # sql_2 = "SELECT * FROM sign_event LIMIT 0,3"
    # result = HandleMsql().run(sql_1, args=(id,))
    # # result = HandleMsql().run(sql_2, is_more=True)
    # print(result)
    do_mysql = HandleMsql()
    print("数据库没有：{}".format(do_mysql.create_not_existesd_id()))
    # print(do_mysql.obtain_existesd_id())
