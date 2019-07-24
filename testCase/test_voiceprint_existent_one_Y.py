#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from testCase.test_get_token_B import Test_get_Token
from framework.testPage import Phone
from testCase.test_group_create_G import Test_Group_create
from testCase.test_file_upload_N import Test_file_upload
from testCase.test_register_Q import Test_register
import os
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_voiceprint_delete").getlog()


class Test_existents_one(unittest.TestCase):
    '''接口名称: existent/one'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")


    @unittest.skip("for a while mode")
    def test_existent_one(self):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])
        # print(appid)
        # fileid=Test_register().test_registers()
        # fileid1=str(fileid[0])
        # print(fileid1)


        access_token=Test_get_Token().test_get_tokens()

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        excel = ReadExcel("existent_one")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus
        self.url=browser+"/api/app/voiceprint/existent/one"




        t = testApi()
        for i in range(0, row - 1):
            if status[i] == '执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                response = t.http_request(url=self.url,data=dict_data,method=method[i], encryption=buer_i,)
                print(response.text)
                result = response.json()["flag"]

                self.assertEqual(result, bool(state_code[i]))

                if result == bool(state_code[i]):
                    RESULT = 'PASS'
                else:
                    RESULT = 'FAIL'

                excel.result_write(str(RESULT))
            else:
                print('你规定不执行')


        mylog.info("测试完成")






if __name__=="__main__":
    unittest.main()