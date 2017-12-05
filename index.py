#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import time
import unittest
import os
from shadon.HTMLTestRunner import HTMLTestRunner
from shadon.testsGetApi import testGetApi

class index():
    # 生成测试报告
    def index(self):
        global filename ,rootDir
        filename = 'null'
        rootDir = os.path.dirname(__file__)
        case_path = rootDir+'/src/'
        ptint_path = rootDir+'/print'
        discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
        filename = ptint_path +'/'+ time.strftime("%Y-%m-%d %H_%M_%S") + '_result.html'
        fp = open(filename,'wb')
        runner = HTMLTestRunner(stream=fp,title='接口测试报告:',description='测试用例:')
        runner.run(discover)
        fp.close()
        pass

    # 生成测试文件
    def build(self):
        getApiOb = testGetApi()
        modules = getApiOb.getApiMoudle()
        for list in modules:
            apiClass =getApiOb.getClassName(list)
            #print(apiClass)
            for list1 in apiClass:
                apiFunction =getApiOb.getFunction(list, list1)
                for list2 in apiFunction:
                    print(list+'/'+list1+'/'+list2)
                    print('--------------')
                    if list2 != 'accessToken':
                        getApiOb.setApiFile(list, list1,list2)
        pass


if __name__ == "__main__":
    shadon = index()
    shadon.build()
    #shadon.index()