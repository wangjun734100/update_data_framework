#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from testCase.test_get_token_B import Test_get_Token
from testCase.test_file_upload_N import Test_file_upload
import os
import time
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_voiceprints_dia").getlog()


class Test_voiceprints_dia(unittest.TestCase):
    '''接口名称: voiceprint/dia'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")


    # @unittest.skip("for a while mode")
    def test_voiceprint_dia(self):
        content = Test_get_Nonce().test_get_nonces()
        self.appid = str(content[0])

        # print(appid)
        file = Test_file_upload().test_file_upload_dia()
        fileid=file[1]



        self.access_token=Test_get_Token().test_get_tokens()

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        excel = ReadExcel("voiceprint_dia")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus
        self.url=browser+"/api/app/voiceprint/dia"



        t = testApi()
        for i in range(0, row - 1):
            if status[i] == '执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                response = t.http_request(url=self.url,data=dict_data,method=method[i], encryption=buer_i,)
                # print(response.text)
                result = response.json()["flag"]

                self.assertEqual(result, bool(state_code[i]))

                if result == bool(state_code[i]):
                    RESULT = 'PASS'
                else:
                    RESULT = 'FAIL'

                excel.result_write(str(RESULT))
                task_id = response.json()["data"]["task_id"]
                # print(task_id)
                return task_id
            else:
                print('你规定不执行')


        mylog.info("测试完成")







if __name__=="__main__":
    unittest.main()