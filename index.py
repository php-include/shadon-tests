# coding:utf-8
import time
import unittest
import os
from shadon.HTMLTestRunner import HTMLTestRunner

class start():
    def index(self):
        #生成测试报告
        global filename ,rootDir
        filename = 'null'
        rootDir = os.path.dirname(__file__)
        # 用例路径
        case_path = rootDir+'/src/Oauth/Controller'
        # 报告路径
        report_path = rootDir+'/print'
        #运行case路径下所有以test开头的文件
        discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
        #print(discover)
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        #报告名称
        filename = report_path +'/'+ now + '_result.html'
        #print(filename)
        fp = open(filename,'wb')
        runner = HTMLTestRunner(stream=fp,title='接口测试报告:',description='测试用例:')
        runner.run(discover)
        fp.close()

if __name__ == "__main__":
    indexs = start()
    indexs.index()