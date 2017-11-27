#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.tsetsHttp import testsHttp
from shadon.testsConfig import testsConfig

class testsToken():
    def __init__(self):
        self.url = '/oauth/authorizationServer/accessToken'
        pass
    def getToken(self):
        pass
    def setToken(self,grant):
        myhttp = testsHttp()
        myhttp.set_url(self.url)
        mytestsConfig = testsConfig()
        mytestsConfig.getConfig()
        self.data = {"grant_type": "client_credentials", "client_id": mytestsConfig.client_id,"client_secret": mytestsConfig.client_secret}

        if grant == 'password':
            mytestsConfig.grant_type = mytestsConfig.getFile('password', 'grant_type')
            mytestsConfig.username = mytestsConfig.getFile('password', 'username')
            mytestsConfig.password = mytestsConfig.getFile('password', 'password')
            self.data = {"grant_type": "password", "client_id": mytestsConfig.client_id,"client_secret": mytestsConfig.client_secret,"username":mytestsConfig.username,"password":mytestsConfig.password}
        print(self.data)
        myhttp.set_data(self.data)
        print(myhttp.post().json())
        pass



if __name__ == "__main__":
    bb = testsToken()
    bb.setToken('client_credentials')