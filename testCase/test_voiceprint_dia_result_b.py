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
mylog = Logger(logger="Test_voiceprints_dia_result").getlog()


class Test_voiceprints_dia_result(unittest.TestCase):
    '''接口名称: voiceprint/dia/result'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")


    # @unittest.skip("for a while mode")
    def test_voiceprint_dia_result(self,interval = 4, time_out = 60):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])

        # print(appid)

        task_id=Test_voiceprints_dia().test_voiceprint_dia()


        access_token=Test_get_Token().test_get_tokens()
        # print(access_token)

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        excel = ReadExcel("dia_result")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus
        self.url=browser+"/api/app/voiceprint/dia/result"



        t = testApi()
        for i in range(0, row - 1):
            if status[i] == '执行':
                dict_data = eval(data[i])
                buer_i = int(buer[i])
                start_time = time.time()
                end_time = start_time + time_out
                count = 1
                while time.time() < end_time:
                    response = t.http_request(url=self.url,data=dict_data,method=method[i], encryption=buer_i)
                    count += 1
                    time.sleep(interval)
                    if response.json()["data"]["result_list"]:
                        break
                else:
                    return None

                # print(response.text)
                result = response.json()["flag"]
                self.assertEqual(result, True)
                result_id_list = []
                if not response:
                    pass
                else:
                    data = response.json()["data"]
                    file_info_list = data["result_list"]
                    for i in range(len(file_info_list)):
                        file_info = file_info_list[i]
                        result_id_list.append(file_info["result_id"])
                # print(result_id_list)
                return result_id_list
            else:
                print('你规定不执行')

        mylog.info("测试完成")


if __name__=="__main__":
    unittest.main()