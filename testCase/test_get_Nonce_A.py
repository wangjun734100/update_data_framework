#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_get_Nonce").getlog()


class Test_get_Nonce(unittest.TestCase):
    '''接口名称:获取nonce'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")



    def test_get_nonces(self):
        config = readConfigFile.ReadConfig()
        browser=config.get_http("browserName")

        excel = ReadExcel("nonce")

        data = excel.getData
        state_code = excel.getStatusCode

        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer = excel.getEncryption
        status = excel.getStatus
        url = browser+"/api/app/auth/get"
        t = testApi()
        try:
            for i in range(0, row - 1):
                if status[i] == '执行':
                    dict_data = eval(data[i])
                    buer_i = int(buer[i])
                    response = t.http_request(url=url, data=dict_data, method=method[i], encryption=buer_i, )
                    # print(response.text)
                    result = response.json()["flag"]

                    self.assertEqual(result, bool(state_code[i]))

                    if result == bool(state_code[i]):
                        RESULT = 'PASS'
                    else:
                        RESULT = 'FAIL'

                    excel.result_write(str(RESULT))
                    nonce = response.json()["data"]["nonce"]
                    # print(nonce)
                    timestamp = response.json()["data"]["timestamp"]
                    # print(timestamp)
                    appid = response.json()["data"]["appid"]
                    # print(appid)
                    appSecret = "7f245af79296093778d40c1bba2caa88"
                    content = [appid, appSecret, nonce, str(timestamp)]

                    return content
                else:
                    print('你规定不执行')
        except Exception as e:
            print(e)




















        mylog.info("测试完成")

if __name__=="__main__":
    unittest.main()


