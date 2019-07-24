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
import os
file = os.path.dirname(os.path.abspath('.')) + '/img/8K_1MIN.wav'
file01 = os.path.dirname(os.path.abspath('.')) + '/img/Register/CA13247391421_800Landline-NoCrossChannel-9b66abc3395943ea89ac52c3cbcbbcd9_20190419163213_phone_vpr_ori_8000.wav'
file02 = os.path.dirname(os.path.abspath('.')) + '/img/sum_92_e4cb82ea273a41b8aab9d5c90ab76298.wav'
file03 = os.path.dirname(os.path.abspath('.')) + '/img/3.wav'



class Test_file_upload(unittest.TestCase):
    '''接口名称: upload upload'''

    def setUp(self):

        print("start")

    def tearDown(self):
        print("end")



    # @unittest.skip("for a while mode")
    def test_file_upload_dia(self):
        content = Test_get_Nonce().test_get_nonces()
        appid = str(content[0])
        # print(appid)
        access_token=Test_get_Token().test_get_tokens()

        # group_id=Test_get_Group().test_get_groups()
        config = readConfigFile.ReadConfig()
        browser=config.get_http("browserName")

        self.url=browser+"/api/app/voiceprint/upload"

        file_path_list=[file01,file02]
        files = {}
        for i in range(len(file_path_list)):
            files["file%s" % str(i)] = ("file%s" % str(i), open(file_path_list[i], "rb"))
        # files={
        #     "file1": ("1562115305.wav", open(file01, "rb"), "audio/wav"),
        #
        # }
        self.headers={
            "user-agent":"PostmanRuntime/7.1.5"

        }
        self.data={
            "appid": appid,
            "access_token": access_token,
            "media_type": "wav",
            "model_type":"model_number_8k",

        }

        response = requests.post(url=self.url, headers=self.headers, data=self.data,files=files,verify=False)
        # print(response.text)
        result=response.json()["flag"]
        self.assertEqual(result,True)
        file_id_list=[]
        if not response:
            pass
        else:
            data = response.json()["data"]
            file_info_list = data["list"]
            for i in range(len(file_info_list)):
                file_info = file_info_list[i]
                file_id_list.append(file_info["fileid"])
        # print(file_id_list)
        return file_id_list




if __name__=="__main__":
    unittest.main()