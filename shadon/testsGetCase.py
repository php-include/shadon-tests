#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import json
import os
import sys

class testsGetCase():
    def __init__(self,moude):
        self.fileName =  os.path.dirname(__file__) + "/../src/SdkTests/" + moude + "/Model/authorizationServerAccessToken.json"
        print()
        self.fileInfo = open(self.fileName, "rb+")
        with open(self.fileName) as json_file:
            data = json.load(json_file)
        self.result = data
        pass

    def getCase(self):
        return self.result

    # 按照索引获取指定期望数据
    def getEcpect(self, index):
        return self.result[index]['ecpect']

    # 按照索引获取指定请求数据
    def getRequest(self, index):
        return self.result[index]['request']


if __name__ == "__main__":
    sdk = testsGetCase('Oauth')
    print(sdk.getCase())
    result = sdk.getEcpect(1)
    print(result)