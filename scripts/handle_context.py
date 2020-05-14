# -*- coding: UTF-8 -*-
"""
======================
@author:fangkun
@time:2020/5/13:17:33
======================
"""
import re
from scripts.handle_mysql import HandleMsql
class Context:
    '''
    做数据参数化
    '''

    not_existed_id_pattern = r'\${not_existed_id}'
    existesd_id_pattern = r'\${invest_user_id}'
    re_name = r'\${not_existed_name}'
    re1_name = r'\${invest_existed_name}'
    @classmethod
    def not_existed_id_replace(cls, data):
        '''
        参数化不存在的id
        :param data:
        :return:
        '''
        if re.search(cls.not_existed_id_pattern, data):
            do_mysql = HandleMsql()
            data = re.sub(cls.not_existed_id_pattern, do_mysql.create_not_existesd_id(), data)

            do_mysql.close()
        return data

    @classmethod
    def invest_user_id(cls, data):
        '''
        参数化存在的id
        :param data:
        :return:
        '''
        if re.search(cls.existesd_id_pattern, data):
            do_mysql = HandleMsql()
            id = do_mysql.obtain_existesd_id()
            data = re.sub(cls.existesd_id_pattern, str(id), data)

            do_mysql.close()
        return data
    @classmethod
    def not_release_conference_name(cls, data):
        '''
        参数不存在的发布会名称
        :param data:
        :return:
        '''
        if re.search(cls.re_name, data):
            do_mysql = HandleMsql()
            data = re.sub(cls.re_name, do_mysql.create_release_conference_name(), data)

            do_mysql.close()
        return data
    @classmethod
    def release_conference_name(cls, data):
        '''
        参数存在的发布会名称
        :param data:
        :return:
        '''
        if re.search(cls.re1_name, data):
            do_mysql = HandleMsql()
            name = do_mysql.obtain_existesd_name()
            data = re.sub(cls.re1_name, str(name), data)

            do_mysql.close()
        return data

    @classmethod
    def readd_parameterization_id(cls, data):
        '''
        参数化不存在和存在的id
        :param data:
        :return:
        '''
        data = cls.not_existed_id_replace(data)
        data = cls.invest_user_id(data)
        data = cls.not_release_conference_name(data)
        data = cls.release_conference_name(data)
        return data

    @classmethod
    def readd_parameterization_name(cls, data):
        '''
        参数化不存在和存在的name
        :param data:
        :return:
        '''
        data = cls.not_release_conference_name(data)
        data = cls.release_conference_name(data)
        return data

if __name__ == '__main__':
    one_str = '{"eid":"${not_existed_id}","name":"${not_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    two_str = '{"eid":"${not_existed_id}","name":"${not_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    three_str = '{"eid":"${not_existed_id}","name":"${not_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    four_str = '{"eid":"","name":"${not_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    five_str = '{"eid":"${invest_user_id}","name":"${not_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'
    six_str = '{"eid":"${not_existed_id}","name":"${invest_existed_name}","limit":"500","status":"1","address":"成都","start_time":"2020-5-30 12:00:00"}'

    # print(Context().readd_parameterization_id(one_str))
    # print(Context().readd_parameterization_id(two_str))
    # print(Context().readd_parameterization_id(three_str))
    # print(Context().readd_parameterization_id(four_str))
    # print(Context().readd_parameterization_id(five_str))
    # print(Context().readd_parameterization_id(six_str))
    # print("------------------------")
    print(Context().readd_parameterization_id(one_str))
    print(Context().readd_parameterization_id(two_str))
    print(Context().readd_parameterization_id(three_str))
    print(Context().readd_parameterization_id(four_str))
    print(Context().readd_parameterization_id(five_str))
    print(Context().readd_parameterization_id(six_str))