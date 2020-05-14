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
from scripts.constants import DATAS_FILE_PATH
from scripts.handle_context import Context

do_excel = handle_excel.HandleExcel(DATAS_FILE_PATH,sheetname="add")
cases = do_excel.get_cases()

@ddt
class GetEvent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.one_session = requests.session()
    @classmethod
    def tearDownClass(cls):
        cls.one_session.close()

    @data(*cases)
    def test_add_event(self, one_case):

        base_url = do_config.get_config("address", "add_address")
        payload = json.loads(Context().readd_parameterization_id(one_case["data"]))
        res = self.one_session.post(base_url, data=payload)
        expected_results = one_case["expected"] #预期结果

        try:
            self.assertEqual(expected_results,res)

        except AssertionError as e:
            raise e

if __name__ == '__main__':
    unittest.main()