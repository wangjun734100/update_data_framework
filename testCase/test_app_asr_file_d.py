#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from testCase.test_get_token_B import Test_get_Token
from testCase.test_file_upload_N import Test_file_upload
from testCase.test_voiceprint_dia_a import Test_voiceprints_dia
import os
import time
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_file_asvcheck").getlog()



class Test_asr_file(unittest.TestCase):
    '''接口名称: /api/app/asr/file'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")


    # @unittest.skip("for a while mode")
    def test_asr_file(self):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])
        file = Test_file_upload().test_file_upload_dia()
        fileid=file[0]

        # print(appid)

        # task_id=Test_voiceprints_dia().test_voiceprint_dia()


        access_token=Test_get_Token().test_get_tokens()
        # print(access_token)

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        excel = ReadExcel("asr_file")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus
        self.url=browser+"/api/app/asr/file"




        t = testApi()

        for i in range(0, row - 1):
            if status[i] == '执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                response = t.http_request(url=self.url, data=dict_data, method=method[i], encryption=buer_i, )
                print(response.text)
                result = response.json()["flag"]

                self.assertEqual(result, bool(state_code[i]))

                if result == bool(state_code[i]):
                    RESULT = 'PASS'
                else:
                    RESULT = 'FAIL'

                excel.result_write(str(RESULT))
                # result_id=response.json()["data"]["result_list"][0]["result_id"]
                # return result_id

            else:
                print('你规定不执行')

        mylog.info("测试完成")







if __name__=="__main__":
    unittest.main()