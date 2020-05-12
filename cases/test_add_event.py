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

do_excel = handle_excel.HandleExcel(DATAS_FILE_PATH,sheetname="add")
cases = do_excel.get_cases()

@ddt
class GetEvent(unittest.TestCase):

    @data(*cases)
    def test_add_event(self, one_case):
        base_url = do_config.get_config("address", "add_address")
        payload = one_case["data"]
        data_dict = json.loads(payload) #将json转换为字典
        msg = one_case["title"]
        expected_results = one_case["expected"] #预期结果
        success_msg = do_config.get_config("msg", "success_result") #pass
        fail_msg = do_config.get_config("msg", "Fail_result") #fail
        try:
            r = requests.post(base_url, data=data_dict)
            self.result = r.json()
            self.assertEqual(expected_results,self.result['message'])
            do_log.info("test_get_event:{} ,测试结果为 {}".format(msg, success_msg))
            do_excel.write_result(one_case['case_id'] + 1, self.result['message'], success_msg)
        except AssertionError as e:
            do_log.error("test_get_event:{} ,测试结果为 {}.具体异常为{}".format(msg,fail_msg,e))
            do_excel.write_result(one_case['case_id'] + 1, self.result['message'], fail_msg)
            raise e

if __name__ == '__main__':
    unittest.main()