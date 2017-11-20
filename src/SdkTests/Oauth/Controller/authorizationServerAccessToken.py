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

class authorizationServerAccessToken(unittest.TestCase):
    def __init__(self):
        self.url =''
        pass
    def openUrl(self):
        pass
    def postUrl(self,request):
        self.getPostData =requests.post(self.url,request)
        pass
    def getSdkJson(self):
        self.result = getSdkJson.getJson(self)
        return self.result
        pass
    def diff(self):
        self.getSdkJson()
        print (self.result)
        self.diff =[]
        for index in len(list(self.result)):
            #thisResult = self.postUrl(self.url, self.result[index]['request']);
            #self.diff.append(thisResult);
            #self.assertEqual(self.diff,self.result[index]['ecpect'])
            print(index)
        pass



if __name__ == "__main__":
   aut =authorizationServerAccessToken()
   aut.diff()