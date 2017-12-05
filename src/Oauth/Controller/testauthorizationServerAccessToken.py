#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# Author: php-include
# Created Time: 20171118
"""
获取 api 测试需要的 token
"""
import unittest
from shadon.testsGetCase import testsGetCase
from shadon.tsetsHttp import testsHttp
from shadon.testsToken import testsToken

class testauthorizationServerAccessTokenTest(unittest.TestCase):
    def setUp(self):
        self.url='/oauth/authorizationServer/accessToken'

    def test_diff(self):
        CaseOb = testsGetCase('Oauth','authorizationServer','accessToken')
        # 拿用例
        cases = CaseOb.getCase()
        myhttp = testsHttp()
        # 拿token
        token = testsToken().getToken()
        myhttp.set_url(self.url)
        header = {"authorization": token}
        myhttp.set_headers(header)
        #获取测试用例
        for index in cases:
            #设置其中一个用例请求参数
            myhttp.set_data(index['request'])
            #请求接口
            thisResult = myhttp.post()
            testresult = thisResult.json()
            #对比测试结果和用例区别
            for myecpect in index['ecpect']:
                if index['ecpect'][myecpect] != testresult[myecpect]:
                    self.assertEqual(index['ecpect'][myecpect] , "*", '案例设置非空不为*')
                    self.assertIsNot(testresult[myecpect],'null',"为空")
                else:
                    self.assertEqual(index['ecpect'][myecpect],testresult[myecpect])
        pass



if __name__ == "__main__":
   aut =testauthorizationServerAccessTokenTest()
   aut.test_diff()