#-*- coding:utf-8 -*-
# 获取模型层配置的参数和期望值
import json
import os
class getSdkJson:
    def __init__(self):
        pass

    def getJson(self):
        self.fileName = os.path.dirname(os.getcwd()) + "/Model/authorizationServerAccessToken.json"
        self.fileInfo = open(self.fileName, "rb+")
        with open(self.fileName) as json_file:
            data = json.load(json_file)
        self.result = data
        return data
    # 按照索引获取指定期望数据
    def getEcpect(self, index):
        return self.result[index]['ecpect']

    # 按照索引获取指定请求数据
    def getRequest(self, index):
        return self.result[index]['request']




if __name__ == "__main__":
   sdk =getSdkJson()
   print(sdk.getJson())
   result =sdk.getEcpect(1)
   print(result)