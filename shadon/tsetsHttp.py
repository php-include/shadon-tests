#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.testsConfig import testsConfig
import requests

class testsHttp ():
    def __init__(self):
        global host, port, timeout
        host = testsConfig().getFile('dev','api_url')
        port = testsConfig().getFile('dev','port')
        timeout = testsConfig().getFile('dev',"timeout")
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            print("Time out!")
            return None

    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            print("Time out!")
            return None


if __name__ == "__main__":
    aa = testsHttp()
    aa.set_url('/oauth/authorizationServer/accessToken')
    print(aa.url)
    print(aa.post())