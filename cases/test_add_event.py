# -*- coding: UTF-8 -*-
# @Time : 2020/5/8 12:24
# @Author : fangkun
# @File : test_get_event.py
# @Software: PyCharm

import unittest
import requests
import json
from libs.ddt import ddt,data
from scripts.handle_config import do_config
from scripts import handle_excel
from scripts.handle_log import do_log
from scripts.constants import DATAS_FILE_PATH
from scripts.handle_context import Context
from scripts.handle_request import HandleRequest

do_excel = handle_excel.HandleExcel(DATAS_FILE_PATH,sheetname="add")
cases = do_excel.get_cases()

@ddt
class GetEvent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.one_session = HandleRequest()
        do_log.info("{:=^40s}".format("用例开始执行"))
    @classmethod
    def tearDownClass(cls):
        cls.one_session.close()
        do_log.info("{:=^40s}".format("用例执行结束"))

    @data(*cases)
    def test_add_event(self, one_case):
        base_url = do_config.get_config("address", "add_address")
        payload = Context().readd_parameterization_id(one_case["data"])
        self.res = (self.one_session.to_request(base_url, data=payload, method='post')).json()

        expected_results = json.loads(one_case["expected"]) #预期结果
        msg = one_case['title']
        try:
            self.assertEqual(expected_results,self.res)
            do_excel.write_result(one_case['case_id'] + 1, self.res['message'], "Pass")
            do_log.info("test_add_event:{} ,测试结果为 {}".format(msg, "Pass"))
        except AssertionError as e:
            do_excel.write_result(one_case['case_id'] + 1, self.res['message'], "Fail")
            do_log.info("test_add_event:{} ,测试结果为 {}".format(msg, "Fail"))
            raise e

if __name__ == '__main__':
    unittest.main()