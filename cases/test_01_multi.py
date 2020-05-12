#使用ddt来进行数据驱动
#根据用例的数量来自动生成实例方法，批量执行用例
import unittest
from lemon_handle_log.ddt import ddt, data
from lemon_handle_log.csdemo import Jisuan
from lemon_handle_log.lemon_03_handleexcel import HandleExcel
from lemon_handle_log.handle_config import do_config
from lemon_handle_log.handle_log import do_log

do_excel = HandleExcel(do_config.get_config("file path", "cases_path"),do_config.get_config("file path", "sheet_name"))
cases = do_excel.get_cases()
@ddt
class Test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # wenjian = do_config.get_config("file path", "log_path")
        # cls.rizhi = open(wenjian,"a",encoding="utf8")
        # cls.rizhi.write("\n{:=^40s}\n".format("测试用例开始执行"))
        do_log.info("\n{:=^40s}".format("测试用例开始执行"))

    @classmethod
    def tearDownClass(cls):
        # cls.rizhi.write("{:=^40s}\n".format("测试用例执行结束"))
        # cls.rizhi.close()
        do_log.info("\n{:=^40s}".format("测试用例开始执行"))

    @data(*cases) #拆包   这里相当于for循环 每拆一次是一个元组会赋值给one_case
    def test_ride(self,one_case):
        actual_results = Jisuan(one_case['l_data'], one_case['r_data']).ride()
        msg = one_case['title']
        expected_results = one_case['expected']
        success_msg = do_config.get_config("msg", "success_result")
        fail_msg = do_config.get_config("msg", "Fail_result")
        try:
            self.assertEqual(expected_results,actual_results, msg=msg)
            # self.rizhi.write("test_ride:{} ,测试结果为 {}\n".format(msg,success_msg))
            do_log.info("test_ride:{} ,测试结果为 {}\n".format(msg, success_msg))
            do_excel.write_result(one_case['case_id']+1,actual_results,success_msg)
        except AssertionError as e:
            # self.rizhi.write("test_ride:{} ,测试结果为 {}.具体异常为{}\n".format(msg,fail_msg,e))
            do_log.error("test_ride:{} ,测试结果为 {}.具体异常为{}\n".format(msg,fail_msg,e))
            do_excel.write_result(one_case['case_id'] + 1, actual_results, fail_msg)
            raise e #因为上面捕获了异常，所以这里用raise来返回异常

if __name__ == '__main__':
    unittest.main()
    #执行了多少条用例，用例条数与data装饰器的（位置）参数个数一致
    #ddt和data是黄金搭档，要一起使用才行