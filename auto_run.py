import unittest
import time
from HTMLTestRunner import HTMLTestRunner

# 定义测试用例所在目录
test_dir = './test_cases'
suit = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

class AutoRun(unittest.TestCase):

    def test_run(self):
        print("程序入口 >>>>>>>>>>>>>")
        cur_time = time.strftime("%Y-%m-%d %H-%M-%S")#将当前时间按照指定的格式转为字符串
        # fp = open('./test_report/report_'+cur_time+'.html', 'wb')
        fp = open('./test_report/report.html', 'wb')
        runner = HTMLTestRunner(stream=fp,
                                title='【pyse_unittest_ddt】Test Report',
                                description='Describe: 测试HTMLTestRunner类库生成测试报告！')
        runner.run(suit, rerun=0, save_last_run=False)
        fp.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)