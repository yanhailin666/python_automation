import os
import unittest,time
from faction import HTMLTestRunner


class AllTest:

    def run(self):
        """
        run test
        :return:
        """
        #获取RunALL.py的父目录
        proDir = os.path.split(os.path.realpath(__file__))[0]
        print(proDir)
        #用例的目录
        self.caseFile = os.path.join(proDir, 'TestCases')
        print(self.caseFile)

        #建立一个测试集
        suite_module = []
        #建立一个测试套件，测试套件没有任何的值，只是一个测试集对象
        test_suite = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(self.caseFile, pattern='*.py', top_level_dir=None)
        print(discover)
        # 构建测试集
        #module里面存储的是py文件
        suite_module.append(discover)
        if len(suite_module) > 0:
            #循环读取每个.py文件
            for suite in suite_module:
                #内循环，循环读取里面的test开头用例
                for test_name in suite:
                    #把用例添加到测试集里面
                    test_suite.addTest(test_name)



        try:
            #判断我用例要不要运行
            if test_suite is not None:
                #设置报告存放的路径
                proDir = os.path.split(os.path.realpath(__file__))[0]
                print(proDir)
                time_code=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())## 返回有格式的日期，要用日期命名文件时，不能有< > / \ | : " * ?；
                report=str(r'timetest\\'+time_code+'.html')
                resultPath=os.path.join(proDir,report)
                print(resultPath)

                #打开报告的文件
                fp = open(resultPath, 'wb')
                #把结果设置写入到report.html
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='测试详情')
                #运行用例
                runner.run(test_suite)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
        finally:
            print("*********TEST END*********")
            #fp.close()

if __name__ == '__main__':
    obj = AllTest()
    obj.run()
