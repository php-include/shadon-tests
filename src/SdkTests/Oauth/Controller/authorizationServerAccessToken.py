#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# Author: php-include
# Created Time: 20171118
"""
获取 api 测试需要的 token
"""

import time
from time import ctime,sleep
import json
from src.SdkTests.Oauth.Model.getSdkJson import getSdkJson
import requests
import unittest
from  shadon.tsetsHttp import testsHttp

class authorizationServerAccessToken(unittest.TestCase):
    def __init__(self):
        self.url ='/oauth/authorizationServer/accessToken'
        pass
    def openUrl(self):
        pass
    def postUrl(self,request):
        return requests.post(self.url,request)
        pass
    def getSdkJson(self):
        self.result = getSdkJson.getJson(self)
        return self.result
        pass
    def diff(self):
        self.getSdkJson()
        for index in self.result:
            aa = testsHttp()
            aa.set_url(self.url)
            print(aa.url)
            testsHttp().set_data(index['request'])
            thisResult = testsHttp().post()
            testresult = thisResult.json()
            for myecpect in index['ecpect']:
                #print(testresult[myecpect])
                print(index['ecpect'][myecpect])
                if index['ecpect'][myecpect] == '*' :
                    print(2)


        pass



if __name__ == "__main__":
   aut =authorizationServerAccessToken()
   aut.diff()