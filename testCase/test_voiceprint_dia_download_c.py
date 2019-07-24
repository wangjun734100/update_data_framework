#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from testCase.test_get_token_B import Test_get_Token
from testCase.test_voiceprint_dia_result_b import Test_voiceprints_dia_result
import logging
import time
from testCase.test_voiceprint_dia_a import Test_voiceprints_dia
import os
import datetime
filepath=os.path.dirname(os.path.abspath('.')) + '/testFile/config.wav'
# if not os.path.exists(filepath):
#     os.makedirs(filepath)


class Test_voiceprints_dia_download(unittest.TestCase):
    '''接口名称: voiceprint/dia/download'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")


    # @unittest.skip("for a while mode")
    def test_voiceprint_dia_download(self):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])
        # print(appid)

        result_id = Test_voiceprints_dia_result().test_voiceprint_dia_result()
        resultid = result_id[0]
        access_token = Test_get_Token().test_get_tokens()

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        self.url = browser + "/api/app/voiceprint/dia/download"

        self.headers = {
            "appid": appid,
            "access-token": access_token,
            "fileid": resultid
        }
        response = requests.post(url=self.url, headers=self.headers, verify=False)
        print(response.content)
        with open(filepath, "wb") as code:
            code.write(response.content)






if __name__=="__main__":
    unittest.main()