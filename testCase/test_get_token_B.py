#-*-coding:GBK -*-
import requests
import unittest
import json
from framework.testApiUpdate import testApi
from framework import readConfigFile
from testCase.test_get_Nonce_A import Test_get_Nonce
from Cryptodome.Hash import SHA256
from framework.readExcel import ReadExcel
from framework.logger import Logger
mylog = Logger(logger="Test_get_Token").getlog()



class Test_get_Token(unittest.TestCase):
    '''接口名称:token'''

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")



    def test_get_tokens(self):
        content=Test_get_Nonce().test_get_nonces()
        # print(content)
        timestamp=int(content[3])
        # print(timestamp)
        nonce=str(content[2])
        appid=str(content[0])
        h=SHA256.new()
        content.sort()
        h.update("".join(content).encode("utf8"))
        signature = h.hexdigest()
        # print(type(signature))

        config = readConfigFile.ReadConfig()
        browser=config.get_http("browserName")
        excel = ReadExcel("token")


        data = excel.getData
        state_code = excel.getStatusCode




        # url = excel.getUrl
        # print(url)
        method = excel.getMethod

        row = excel.getRows
        buer=excel.getEncryption
        status=excel.getStatus

        self.url=browser+"/api/app/auth/token/get"

        # t = testApi()
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
                    access_token = response.json()["data"]["access_token"]
                    # print(access_token)
                    return access_token

                else:
                    print('你规定不执行')
        except Exception as e:
            print(e)


    mylog.info("测试完成")




if __name__=="__main__":
    unittest.main()
