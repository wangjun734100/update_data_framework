#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from testCase.test_get_token_B import Test_get_Token
from framework.testPage import Phone
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_Group_create").getlog()


class Test_Group_create(unittest.TestCase):
    '''接口名称:create group'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")



    def test_groups_create(self):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])
        # print(appid)
        access_token=Test_get_Token().test_get_tokens()
        group_name=Phone().phoneRandom()
        group_text=Phone().textRandom()
        config = readConfigFile.ReadConfig()
        browser = config.get_http("browserName")
        excel = ReadExcel("group_create")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus

        self.url=browser+"/api/app/group/create"


        t = testApi()
        try:
            for i in range(0, row - 1):
                if status[i] == '执行':
                    dict_data = eval(data[i])
                    buer_i = int(buer[i])
                    response = t.http_request(url=self.url, data=dict_data, method=method[i], encryption=buer_i, )
                    # print(response.text)
                    result = response.json()["flag"]

                    self.assertEqual(result, bool(state_code[i]))

                    if result == bool(state_code[i]):
                        RESULT = 'PASS'
                    else:
                        RESULT = 'FAIL'

                    excel.result_write(str(RESULT))
                    group_id = response.json()["data"]["groupid"]
                    return group_id
                else:
                    print('你规定不执行')
        except Exception as e:
            print(e)


        mylog.info("测试完成")



if __name__=="__main__":
    unittest.main()