#-*- coding:utf-8 -*-
import unittest
from src.SdkTests.Oauth.Controller.authorizationServerAccessToken import authorizationServerAccessToken

class tests(unittest.TestCase):
    def testAuthorizationServerAccessToken(self):
        self.log = authorizationServerAccessToken.getdiff(self)
        print(111)
        pass



if __name__ == "__main__":
    tests1 = tests()
    tests1.testAuthorizationServerAccessToken()