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

class testauthorizationServerAccessToken(unittest.TestCase):
    def __init__(self):
        self.url ='/oauth/authorizationServer/accessToken'
        super().__init__()
        pass
    def diff(self):
        CaseOb = testsGetCase('Oauth')
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
                print(myecpect)
                if index['ecpect'][myecpect] != testresult[myecpect]:
                   print(1)

                   self.assertEqual(1 , 1, 'ssss')

        pass



if __name__ == "__main__":
   aut =testauthorizationServerAccessToken()
   aut.diff()