#!/usr/bin/evn python
# -*- coding:utf-8 -*-


class testsEnv():
    def __init__(self):
        self.env='dev'
        pass
    def getEnv(self):
        return self.env
        pass
    def setEnv(self,env):
        self.env = env
        pass




if __name__ == "__main__":

    env =testsEnv()
    env.setEnv("test")
    print(env.env)
