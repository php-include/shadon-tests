#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.tsetsHttp import testsHttp
from shadon.testsConfig import testsConfig
import os

class testsToken():
    def __init__(self):
        self.url = '/oauth/authorizationServer/accessToken'
        self.mytestsConfig = testsConfig()
        self.mytestsConfig.getConfig()
        self.path = os.path.dirname(os.getcwd()) + "/config/" + self.mytestsConfig.env + "/sdk/"
        self.grant='client_credentials'
        pass
    def setGrant(self,grant):
        self.grant = grant
        pass

    def getToken(self):
        if os.path.exists(self.path) != True:
            self.setToken(self.grant)
        file = open(self.path + 'token.txt', 'r')
        return file.read()
        pass
    def setToken(self,grant):
        myhttp = testsHttp()
        myhttp.set_url(self.url)
        self.data = {"grant_type": "client_credentials", "client_id": self.mytestsConfig.client_id,"client_secret": self.mytestsConfig.client_secret}

        if grant == 'password':
            self.mytestsConfig.grant_type = self.mytestsConfig.getFile('password', 'grant_type')
            self.mytestsConfig.username = self.mytestsConfig.getFile('password', 'username')
            self.mytestsConfig.password = self.mytestsConfig.getFile('password', 'password')
            self.data = {"grant_type": "password", "client_id": self.mytestsConfig.client_id,"client_secret": self.mytestsConfig.client_secret,"username":self.mytestsConfig.username,"password":self.mytestsConfig.password}

        #print(self.data)
        myhttp.set_data(self.data)
        tokenInfo =myhttp.post().json()
        #print(tokenInfo)
        #如果目录不存在，建立目录
        if os.path.exists(self.path) != True:
            os.makedirs(self.path)
        #写入数据
        file = open(self.path+'token.txt','w')
        file.write(str(tokenInfo))

        pass



if __name__ == "__main__":
    bb = testsToken()
    bb.setToken('passwords')
    print(bb.getToken())