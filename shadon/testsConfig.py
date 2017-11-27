#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import configparser
import os
from shadon.testsEnv import testsEnv

class testsConfig():
    def __init__(self):
        self.env = testsEnv().getEnv()
        self.configDri = self.fileName = os.path.dirname(os.getcwd()) + "/config/" + self.env + "/sdk/sdkConfig.conf"

        pass
    def getFile(self,section,option):
        conf = configparser.ConfigParser()
        conf.read(self.configDri, encoding='utf-8')  # 文件路径
        value = conf.get(section, option)  # 获取指定section 的option值
        return value
    def getConfig(self):
        self.api_url = self.getFile(self.env,'api_url')
        self.port = self.getFile(self.env, 'port')
        self.timeout = self.getFile(self.env, 'timeout')
        self.grant_type = self.getFile(self.env, 'grant_type')
        self.client_id = self.getFile(self.env, 'client_id')
        self.client_secret = self.getFile(self.env, 'client_secret')
        pass

if __name__ == "__main__":
    test = testsConfig()
    print(test.getFile('dev','api_url'))
    test.getConfig()
    print(test.port)