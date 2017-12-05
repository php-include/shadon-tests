#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import os

class testsEnv():
    def __init__(self):
        envDri  = os.path.dirname(__file__) + "/../.env"
        env = None
        if os.path.exists(envDri) == True:
            file = open(envDri, 'r')
            env = file.read()
        if env != None:
            self.env=env
        else:
            self.env='dev'
        pass

    def getEnv(self):
        return self.env

    def setEnv(self,env):
        self.env = env
        pass


if __name__ == "__main__":

    env =testsEnv()
    env.setEnv("dev")
    print(env.getEnv())
