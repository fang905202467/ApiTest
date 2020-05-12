# -*- coding: UTF-8 -*-
# @Time : 2020/5/12 10:43 
# @Author : fangkun
# @File : handle_mysql.py 
# @Software: PyCharm

import pymysql
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

if __name__ == '__main__':
    id = 2
    sql_1 = "SELECT * FROM sign_event WHERE id=%s"
    sql_2 = "SELECT * FROM sign_event LIMIT 0,3"
    result = HandleMsql().run(sql_1, args=(id,))
    # result = HandleMsql().run(sql_2, is_more=True)
    print(result)